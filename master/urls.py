# master/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from master.views import ContentViewSet, CountryViewSet, CourseCategoryViewSet, CourseSubCategoryViewSet, FAQCategoryViewSet, PackageContentViewSet, PackageViewSet, ServiceCategoryViewSet, StateViewSet, CityViewSet, BankViewSet, DepartmentViewSet, DesignationViewSet, SocialStatusViewSet, DocumentTypeViewSet, DocumentViewSet, BranchTypeViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'banks', BankViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'designations', DesignationViewSet)
router.register(r'socialstatus', SocialStatusViewSet)
router.register(r'document_types', DocumentTypeViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'branch_types', BranchTypeViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'package_contents', PackageContentViewSet)
router.register(r'service_categories', ServiceCategoryViewSet)
router.register(r'course_categories', CourseCategoryViewSet)
router.register(r'course_sub_categories', CourseSubCategoryViewSet)
router.register(r'faq_categories', FAQCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
