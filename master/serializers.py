# master/serilizers.py

from rest_framework import serializers
from utils.serializers import SlugValidationMixin
from master.models import Content, Country, CourseCategory, CourseSubCategory, FAQCategory, Package, PackageContent, ServiceCategory, State, City, Bank, Department, Designation, SocialStatus, DocumentType, Document, BranchType

class CountrySerializer(SlugValidationMixin, serializers.ModelSerializer):    
    slug_source_field = ['iso3']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['country', 'name']
    country_name = serializers.CharField(source='country.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['country', 'state', 'name']
    country_name = serializers.CharField(source='country.name', read_only=True)
    state_name = serializers.CharField(source='state.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class BankSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['country', 'name']
    country_name = serializers.CharField(source='country.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Bank
        fields = '__all__'


class DepartmentSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['name']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class DesignationSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['title']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Designation
        fields = '__all__'


class SocialStatusSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['title']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = SocialStatus
        fields = '__all__'


class DocumentTypeSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['type']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['document_type', 'name']
    document_type_name = serializers.CharField(source='document_type.type', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'


class BranchTypeSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['type']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = BranchType
        fields = '__all__'


class PackageSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['name']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Package
        fields = '__all__'


class ContentSerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['content']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class PackageContentSerializer(SlugValidationMixin, serializers.ModelSerializer):
    package_name = serializers.CharField(source='package.name', read_only=True)
    content_name = serializers.CharField(source='content.content', read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = PackageContent
        fields = '__all__'


class ServiceCategorySerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['category']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = ServiceCategory
        fields = '__all__'


class CourseCategorySerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['category']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseSubCategorySerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['category', 'sub_category']
    category_name = serializers.CharField(source='category.category', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = CourseSubCategory
        fields = '__all__'


class FAQCategorySerializer(SlugValidationMixin, serializers.ModelSerializer):
    slug_source_field = ['category']
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = FAQCategory
        fields = '__all__'