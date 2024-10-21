# utils/serializers.py

from rest_framework import serializers
from django.utils.text import slugify

class SlugValidationMixin:
    slug_source_field = None  # Field(s) used to generate the slug
    slug_field = 'slug'       # Name of the slug field in the model

    def generate_slug(self, validated_data):
        values = []

        # Handle foreign key fields properly (like 'country__iso3')
        for field in self.slug_source_field:
            if '__' in field:
                related_field, attr = field.split('__')
                related_obj = validated_data.get(related_field)
                if related_obj:
                    values.append(getattr(related_obj, attr, ''))
            else:
                values.append(validated_data.get(field, '') or '')

        # Join the values and generate a slug
        return slugify('-'.join(str(value) for value in values if value))

    def validate(self, attrs):
        ModelClass = self.Meta.model

        # Check if the model has the slug field and slug_source_field is specified
        if self.slug_field in [field.name for field in ModelClass._meta.get_fields()] and self.slug_source_field:
            regenerate_slug = True if not self.instance else False

            if regenerate_slug:
                slug = self.generate_slug(attrs)
                attrs[self.slug_field] = slug

                # Check for uniqueness of the slug
                queryset = ModelClass.objects.filter(**{self.slug_field: slug})
                if self.instance:
                    queryset = queryset.exclude(pk=self.instance.pk)
                if queryset.exists():
                    raise serializers.ValidationError(f"Slug '{slug}' already exists.")

            else:
                attrs[self.slug_field] = getattr(self.instance, self.slug_field)

        return super().validate(attrs)
