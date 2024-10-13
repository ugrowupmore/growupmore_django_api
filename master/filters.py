# master/filters.py

from utils.filters import BaseFilterSet, get_non_image_fields
from master.models import (
    Content, CourseCategory, CourseSubCategory, DocumentType, Document, Country, FAQCategory, Package, PackageContent, ServiceCategory, State, City, Bank, Department, Designation, SocialStatus, BranchType
)

class DocumentTypeFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = DocumentType
        fields = get_non_image_fields(DocumentType)

class DocumentFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Document
        fields = get_non_image_fields(Document)

class CountryFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Country
        fields = get_non_image_fields(Country)

class StateFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = State
        fields = get_non_image_fields(State)

class CityFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = City
        fields = '__all__'

class BankFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Bank
        fields = '__all__'

class DepartmentFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Department
        fields = '__all__'

class DesignationFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Designation
        fields = '__all__'

class SocialStatusFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = SocialStatus
        fields = '__all__'

class BranchTypeFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = BranchType
        fields = get_non_image_fields(BranchType)

class PackageFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Package
        fields = '__all__'


class ContentFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = Content
        fields = '__all__'


class PackageContentFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = PackageContent
        fields = '__all__'


class ServiceCategoryFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = ServiceCategory
        fields = '__all__'


class CourseCategoryFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = CourseCategory
        fields = '__all__'


class CourseSubCategoryFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = CourseSubCategory
        fields = '__all__'


class FAQCategoryFilter(BaseFilterSet):
    class Meta(BaseFilterSet.Meta):
        model = FAQCategory
        fields = '__all__'
