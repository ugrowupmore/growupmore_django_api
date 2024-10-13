# hr/filters.py

from utils.filters import BaseFilterSet, get_non_image_fields
from django_filters import rest_framework as filters
from hr.models import Employee

class EmployeeFilter(BaseFilterSet):
    class Meta:
        model = Employee
        fields = get_non_image_fields(Employee)