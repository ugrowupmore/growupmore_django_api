# utils/soft_delete.py

import os
from django.core.exceptions import ValidationError
from django.db import models
from utils.basemodel import BaseModel


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        # Exclude soft-deleted records by default
        return super().get_queryset().filter(is_deleted=False)

class SoftDeleteModel(BaseModel):    
    objects = SoftDeleteManager()  # Default manager excluding soft-deleted records
    all_objects = models.Manager()  # Manager including all records

    def delete(self, *args, **kwargs):
        """Soft delete by setting is_deleted to True."""
        self.is_deleted = True
        self.save()

    def restore(self, *args, **kwargs):
        """Restore the soft-deleted record by setting is_deleted to False."""
        self.is_deleted = False
        self.save()

    def remove_old_image(self, image_field):
        """Delete the old image file from the file system."""
        if image_field and hasattr(image_field, 'path') and os.path.isfile(image_field.path):
            os.remove(image_field.path)

    def handle_image_update(self, field_name):
        """Handles the logic of removing old images when an image is updated or set to null."""
        try:
            # Retrieve the current instance from the database
            current_instance = self.__class__.all_objects.get(pk=self.pk)
            old_image = getattr(current_instance, field_name)
            new_image = getattr(self, field_name)

            # If the image has changed, remove the old one
            if old_image and old_image != new_image:
                self.remove_old_image(old_image)
        except self.__class__.DoesNotExist:
            # Instance does not exist in the database, no action needed
            pass

    def validate_unique_image_name(self, field_name):
        """Validate that an image with the same name does not already exist."""
        image_field = getattr(self, field_name)
        if image_field:
            existing = self.__class__.objects.filter(**{f"{field_name}__exact": image_field.name}).exclude(pk=self.pk)
            if existing.exists():
                raise ValidationError(f"Image with name '{image_field.name}' already exists.")

    def clean(self):
        """Automatically validate uniqueness of image fields."""
        for field in self.get_image_fields():
            self.validate_unique_image_name(field)

    def save(self, *args, **kwargs):
        """Automatically handle image updates and deletion."""
        for field in self.get_image_fields():
            self.handle_image_update(field)
        super().save(*args, **kwargs)

    def get_image_fields(self):
        """Return a list of image fields for the model."""
        return [field.name for field in self._meta.fields if isinstance(field, models.ImageField)]

    class Meta:
        abstract = True