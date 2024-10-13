# utils/filters.py

from django_filters import rest_framework as filters
from django.db import models

class BaseFilterSet(filters.FilterSet):
    """
    Centralized FilterSet that overrides ImageField to use CharFilter.
    """
    class Meta:
        abstract = True
        filter_overrides = {
            models.ImageField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'exact',
                },
            },            
            models.CharField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.JSONField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }

def get_non_image_fields(model):
    """Utility function to get all field names excluding ImageFields."""
    return [field.name for field in model._meta.fields if not isinstance(field, models.ImageField)]
