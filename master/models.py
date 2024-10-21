# master/models.py

from django.db import models
from django.utils.text import slugify
from hr.models import Employee
from utils.enums import DesignationLevel
from utils.image_size import validate_image_size_2mb
from utils.soft_delete import SoftDeleteModel

# Country model
class Country(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    numeric_code = models.TextField(default='NA')
    iso2 = models.TextField(default='NA')
    iso3 = models.TextField(default='NA', unique=True, )
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    phone_code = models.TextField(default='NA')
    capital = models.IntegerField(default=0)
    currency = models.TextField(default='NA')
    currency_name = models.TextField(default='NA')
    currency_symbol = models.TextField(default='NA')
    national_language = models.TextField(default='NA')
    nationality = models.TextField(default='NA')
    languages = models.JSONField(default=list)
    tld = models.TextField(default='NA')
    flag_image = models.ImageField(upload_to='countries_flags/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    founded_date = models.DateField(null=True, blank=True)
    website = models.TextField(default='NA')   

    class Meta:
        db_table = '"master"."countries"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['iso2']),
            models.Index(fields=['iso3']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(Country, self).save(*args, **kwargs)

        # Check if is_active has changed
        if not self.is_active:            
            State.objects.filter(country=self).update(is_active=False)
            City.objects.filter(country=self).update(is_active=False)
            Employee.objects.filter(country=self).update(is_active=False)


        if not self.is_deleted:            
            State.objects.filter(country=self).update(is_deleted=False)
            City.objects.filter(country=self).update(is_deleted=False)   
            Employee.objects.filter(country=self).update(is_deleted=False)      

    def __str__(self):
        return self.name

# State model
class State(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='states')
    name = models.TextField(default='NA')
    capital = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    flag_image = models.ImageField(upload_to='states_flags/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    founded_date = models.DateField(null=True, blank=True)
    website = models.TextField(default='NA')   

    class Meta:
        db_table = '"master"."states"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(State, self).save(*args, **kwargs)

        # Ensure country is_active is True if state is_active is set to True
        if self.is_active:
            if self.country and not self.country.is_active:
                self.country.is_active = True
                self.country.save()

        # Ensure country is_deleted is False if state is_deleted is set to False
        if not self.is_deleted:
            if self.country and self.country.is_deleted:
                self.country.is_deleted = False
                self.country.save()

        # Check if is_active has changed
        if not self.is_active:
            City.objects.filter(state=self).update(is_active=False)
            Employee.objects.filter(state=self).update(is_active=False)

        if not self.is_deleted:
            City.objects.filter(state=self).update(is_deleted=False)
            Employee.objects.filter(state=self).update(is_deleted=False)

    def __str__(self):
        return self.name


# City model
class City(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='cities')
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL, related_name='cities')
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, default=0)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, default=0)
    location_url = models.TextField(default='NA')
    phonecode = models.IntegerField(default=0)
    population = models.BigIntegerField(default=0)
    timezone = models.TextField(default='NA')
    founded_date = models.DateField(null=True, blank=True)
    website = models.TextField(default='NA')   

    class Meta:
        db_table = '"master"."cities"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(City, self).save(*args, **kwargs)

        # Ensure state and country are_active is True if city is_active is set to True
        if self.is_active:
            if self.state and not self.state.is_active:
                self.state.is_active = True
                self.state.save()

            if self.country and not self.country.is_active:
                self.country.is_active = True
                self.country.save()

        # Ensure state and country are_deleted is False if city is_deleted is set to False
        if not self.is_deleted:
            if self.state and self.state.is_deleted:
                self.state.is_deleted = False
                self.state.save()

            if self.country and self.country.is_deleted:
                self.country.is_deleted = False
                self.country.save()

        # Check if is_active has changed
        if not self.is_active:            
            Employee.objects.filter(city=self).update(is_active=False)

        if not self.is_deleted:            
            Employee.objects.filter(city=self).update(is_deleted=False)

    def __str__(self):
        return self.name


# Bank model
class Bank(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='banks')
    swift_code = models.TextField(default='NA')
    iban_code = models.TextField(default='NA')
    description = models.TextField(default='NA')   

    class Meta:
        db_table = '"master"."banks"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):      
        super(Bank, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name


# Department model
class Department(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')
   
    class Meta:
        db_table = '"master"."departments"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(Department, self).save(*args, **kwargs)

        # Check if is_active has changed
        if not self.is_active:            
            Employee.objects.filter(department=self).update(is_active=False)

        if not self.is_deleted:            
            Employee.objects.filter(department=self).update(is_deleted=False)

    def __str__(self):
        return self.name
    

# Designation model
class Designation(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    title = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    level = models.CharField(max_length=10, choices=DesignationLevel.choices, default=DesignationLevel.OTHER)
    description = models.TextField(default='NA')
    travel_required = models.BooleanField(default=False)
    training_required = models.BooleanField(default=False)   

    class Meta:
        db_table = '"master"."designations"'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):     
        super(Designation, self).save(*args, **kwargs)

        # Check if is_active has changed
        if not self.is_active:            
            Employee.objects.filter(designation=self).update(is_active=False)

        if not self.is_deleted:            
            Employee.objects.filter(designation=self).update(is_deleted=False)

    def __str__(self):
        return self.title


# SocialStatus model
class SocialStatus(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')   

    class Meta:
        db_table = '"master"."social_status"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(SocialStatus, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# DocumentType model
class DocumentType(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    type = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='doctypes_images/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    description = models.TextField(default='NA')
    
    class Meta:
        db_table = '"master"."document_types"'
        indexes = [
            models.Index(fields=['type']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):      
        super(DocumentType, self).save(*args, **kwargs)

        # Now, perform the related document updates
        if not self.is_active:
            Document.objects.filter(document_type=self).update(is_active=False)

        if not self.is_deleted:
            Document.objects.filter(document_type=self).update(is_deleted=False)

    def __str__(self):
        return self.type


# Document model
class Document(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    document_type = models.ForeignKey(DocumentType, null=True, blank=True, on_delete=models.SET_NULL, related_name='documents')
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='doc_images/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    description = models.TextField(default='NA')
    
    class Meta:
        db_table = '"master"."documents"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):        
        super(Document, self).save(*args, **kwargs)

        # Ensure document_type is_active is True if document is_active is set to True
        if self.is_active:
            if self.document_type and not self.document_type.is_active:
                self.document_type.is_active = True
                self.document_type.save()

        # Ensure document_type is_deleted is False if document is_deleted is set to False
        if not self.is_deleted:
            if self.document_type and self.document_type.is_deleted:
                self.document_type.is_deleted = False
                self.document_type.save()

        # Check if is_active has changed
        if not self.is_active:
            # Additional logic if needed when document is set to inactive
            pass

        if not self.is_deleted:
            # Additional logic if needed when document is undeleted
            pass

    def __str__(self):
        return self.name


# BranchType model
class BranchType(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    type = models.TextField(default='NA', unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='branchtypes_images/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    description = models.TextField(default='NA')
    
    class Meta:
        db_table = '"master"."branch_types"'
        indexes = [
            models.Index(fields=['type']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(BranchType, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


# Packages model
class Package(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."packages"'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):     
        super(Package, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Contents model
class Content(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    content = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."contents"'
        indexes = [
            models.Index(fields=['content']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


# PackageContents model
class PackageContent(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_contents')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='package_contents')
    is_available = models.BooleanField(default=False)

    class Meta:
        db_table = '"master"."package_contents"'
        indexes = [
            models.Index(fields=['package']),
            models.Index(fields=['content']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]
        # Add a unique constraint for the composite key of package and content
        constraints = [
            models.UniqueConstraint(fields=['package', 'content'], name='unique_package_content')
        ]


# ServiceCategories model
class ServiceCategory(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    category = models.TextField(default='NA', unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."service_categories"'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):       
        super(ServiceCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


# CourseCategories model
class CourseCategory(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    category = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."course_categories"'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):      
        super(CourseCategory, self).save(*args, **kwargs)

        # Check if is_active has changed
        if not self.is_active:            
            CourseSubCategory.objects.filter(course_category=self).update(is_active=False)            

        if not self.is_deleted:            
            CourseSubCategory.objects.filter(course_category=self).update(is_deleted=False)    

    def __str__(self):
        return self.category        


# CourseSubCategories model
class CourseSubCategory(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_categories')
    sub_category = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."course_sub_categories"'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['sub_category']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):        
        super(CourseSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.sub_category


# FAQCategories model
class FAQCategory(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    category = models.TextField(default='NA')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"master"."faq_categories"'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        super(FAQCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category
