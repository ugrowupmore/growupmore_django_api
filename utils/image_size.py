# utils/image_size.py

# Image size validator
from django.forms import ValidationError


def validate_image_size_2mb(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise ValidationError("Image file too large (maximum size is 2MB)")