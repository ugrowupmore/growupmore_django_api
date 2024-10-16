# utils/serializers.py

from rest_framework import serializers
from django.utils.text import slugify

class SlugValidationMixin:
    slug_source_field = None  # Field(s) used to generate the slug
    slug_field = 'slug'       # Name of the slug field in the model

    def generate_slug(self, validated_data):
        if isinstance(self.slug_source_field, str):
            value = validated_data.get(self.slug_source_field, '') or ''
            return slugify(value)
        elif isinstance(self.slug_source_field, (list, tuple)):
            values = [str(validated_data.get(field, '') or '') for field in self.slug_source_field]
            return slugify('-'.join(values))
        else:
            raise ValueError("slug_source_field must be a string or list/tuple of strings")

    def validate(self, attrs):
        ModelClass = self.Meta.model

        # Check if the model has the slug field and slug_source_field is specified
        if self.slug_field in [field.name for field in ModelClass._meta.get_fields()] and self.slug_source_field:
            # Determine whether to regenerate the slug
            regenerate_slug = False
            if self.instance:
                # We're updating an existing instance
                for field in self.slug_source_field:
                    if attrs.get(field) != getattr(self.instance, field):
                        regenerate_slug = True
                        break
            else:
                # We're creating a new instance
                regenerate_slug = True

            if regenerate_slug:
                # Generate the slug
                slug = self.generate_slug(attrs)
                attrs[self.slug_field] = slug

                # Check for uniqueness of the slug
                queryset = ModelClass.objects.filter(**{self.slug_field: slug})
                if self.instance:
                    queryset = queryset.exclude(pk=self.instance.pk)
                if queryset.exists():
                    source_fields = self.slug_source_field
                    if isinstance(source_fields, (list, tuple)):
                        field_names = ', '.join(source_fields)
                        field_values = ', '.join(str(attrs.get(field, '')) for field in source_fields)
                        error_message = f"{field_names} ('{field_values}') already exists."
                    else:
                        field_names = source_fields
                        field_values = str(attrs.get(source_fields, ''))
                        error_message = f"{field_names} ('{field_values}') already exists."

                    raise serializers.ValidationError({
                        field_names: error_message
                    })
            else:
                # Keep the existing slug if the source fields haven't changed
                attrs[self.slug_field] = getattr(self.instance, self.slug_field)

        return super().validate(attrs)
