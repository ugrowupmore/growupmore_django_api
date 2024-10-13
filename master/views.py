# master/views.py

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from master.filters import ContentFilter, CountryFilter, CourseCategoryFilter, CourseSubCategoryFilter, DocumentFilter, DocumentTypeFilter, FAQCategoryFilter, PackageContentFilter, PackageFilter, ServiceCategoryFilter, StateFilter
from utils.pagination import StandardResultsSetPagination
from master.models import Content, Country, CourseCategory, CourseSubCategory, FAQCategory, Package, PackageContent, ServiceCategory, State, City, Bank, Department, Designation, SocialStatus, DocumentType, Document, BranchType
from master.serializers import ContentSerializer, CountrySerializer, CourseCategorySerializer, CourseSubCategorySerializer, FAQCategorySerializer, PackageContentSerializer, PackageSerializer, ServiceCategorySerializer, StateSerializer, CitySerializer, BankSerializer, DepartmentSerializer, DesignationSerializer, SocialStatusSerializer, DocumentTypeSerializer, DocumentSerializer, BranchTypeSerializer
from utils.views import SoftDeleteViewSet


class CountryViewSet(SoftDeleteViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  
    filterset_class = CountryFilter  
    filterset_fields = '__all__'
    search_fields = ['name', 'iso2', 'iso3', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'iso2', 'iso3', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class StateViewSet(SoftDeleteViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = StateFilter
    filterset_fields = '__all__'
    search_fields = ['name', 'country__name', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'country__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class CityViewSet(SoftDeleteViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['name', 'state__name', 'country__name', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'state__name', 'country__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class BankViewSet(SoftDeleteViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['name', 'country__name', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'country__name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class DepartmentViewSet(SoftDeleteViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['name', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class DesignationViewSet(SoftDeleteViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['title', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'title', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class SocialStatusViewSet(SoftDeleteViewSet):
    queryset = SocialStatus.objects.all()
    serializer_class = SocialStatusSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['name', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class DocumentTypeViewSet(SoftDeleteViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DocumentTypeFilter
    filterset_fields = '__all__'
    search_fields = ['type', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'type', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class DocumentViewSet(SoftDeleteViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DocumentFilter
    filterset_fields = '__all__'
    search_fields = ['name', 'document_type__type', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'name', 'document_type__type', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class BranchTypeViewSet(SoftDeleteViewSet):
    queryset = BranchType.objects.all()
    serializer_class = BranchTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['type', 'status', 'is_active', 'is_deleted']  # Updated for indexed fields
    ordering_fields = ['id', 'type', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class PackageViewSet(SoftDeleteViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PackageFilter
    search_fields = ['name', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'name', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class ContentViewSet(SoftDeleteViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ContentFilter
    search_fields = ['content', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'content', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class PackageContentViewSet(SoftDeleteViewSet):
    queryset = PackageContent.objects.all()
    serializer_class = PackageContentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PackageContentFilter
    search_fields = ['package__name', 'content__content', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'package__name', 'content__content', 'status', 'is_active', 'is_deleted']
    pagination_class = StandardResultsSetPagination


class ServiceCategoryViewSet(SoftDeleteViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ServiceCategoryFilter
    search_fields = ['category', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'category', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class CourseCategoryViewSet(SoftDeleteViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CourseCategoryFilter
    search_fields = ['category', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'category', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class CourseSubCategoryViewSet(SoftDeleteViewSet):
    queryset = CourseSubCategory.objects.all()
    serializer_class = CourseSubCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CourseSubCategoryFilter
    search_fields = ['category__category', 'sub_category', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'category__category', 'sub_category', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination


class FAQCategoryViewSet(SoftDeleteViewSet):
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = FAQCategoryFilter
    search_fields = ['category', 'status', 'is_active', 'is_deleted']
    ordering_fields = ['id', 'category', 'status', 'is_active', 'is_deleted']
    lookup_field = 'slug'
    pagination_class = StandardResultsSetPagination