# master/serilizers.py

from rest_framework import serializers
from master.models import Content, Country, CourseCategory, CourseSubCategory, FAQCategory, Package, PackageContent, ServiceCategory, State, City, Bank, Department, Designation, SocialStatus, DocumentType, Document, BranchType

class CountrySerializer(serializers.ModelSerializer):        
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    slug_source_field = ['country__iso3', 'name']
    country_name = serializers.CharField(source='country.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):    
    country_name = serializers.CharField(source='country.name', read_only=True)
    state_name = serializers.CharField(source='state.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):    
    country_name = serializers.CharField(source='country.name', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Bank
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Designation
        fields = '__all__'


class SocialStatusSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = SocialStatus
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):    
    document_type_name = serializers.CharField(source='document_type.type', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'


class BranchTypeSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = BranchType
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Package
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class PackageContentSerializer(serializers.ModelSerializer):
    package_name = serializers.CharField(source='package.name', read_only=True)
    content_name = serializers.CharField(source='content.content', read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = PackageContent
        fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = ServiceCategory
        fields = '__all__'


class CourseCategorySerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseSubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category', read_only=True)
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = CourseSubCategory
        fields = '__all__'


class FAQCategorySerializer(serializers.ModelSerializer):    
    slug = serializers.CharField(read_only=True)
    create_date = serializers.DateTimeField(read_only=True)
    last_update_date = serializers.DateTimeField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    class Meta:
        model = FAQCategory
        fields = '__all__'