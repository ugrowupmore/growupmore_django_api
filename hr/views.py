from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from hr.filters import EmployeeFilter
from hr.models import Employee
from hr.serializers import EmployeeSerializer
from utils.pagination import StandardResultsSetPagination

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['first_name', 'last_name', 'department__name', 'designation__title', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'first_name', 'last_name', 'department__name', 'designation__title', 'status', 'is_active', 'is_deleted']
    lookup_field = 'id'
    pagination_class = StandardResultsSetPagination
