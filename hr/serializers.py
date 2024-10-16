# hr/serilizers.py

from rest_framework import serializers
from hr.models import Employee
from utils.serializers import SlugValidationMixin

class EmployeeSerializer(SlugValidationMixin, serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    state_name = serializers.CharField(source='state.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    designation_name = serializers.CharField(source='designation.title', read_only=True)
    manager_name = serializers.CharField(source='manager.first_name', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
