# hr/models.py

from django.db import models
from utils.enums import EmployeeType, WorkSchedule, EmployeeBadge, NationalIDType
from utils.image_size import validate_image_size_2mb
from utils.soft_delete import SoftDeleteModel

class Employee(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(default='NA')
    last_name = models.TextField(default='NA')
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, default='m')
    nationality = models.ForeignKey('master.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_nationality')
    marital_status = models.BooleanField(default=False)
    address = models.TextField(default='NA')
    country = models.ForeignKey('master.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_country')
    state = models.ForeignKey('master.State', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_state')
    city = models.ForeignKey('master.City', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_city')
    zipcode = models.TextField(default='NA')
    personal_contact = models.BigIntegerField(default=0)
    personal_email = models.TextField(default='NA')
    work_contact = models.BigIntegerField(default=0)
    work_email = models.TextField(default='NA')
    emergency_contact = models.BigIntegerField(default=0)
    emergency_contact_relationship = models.TextField(default='NA')
    department = models.ForeignKey('master.Department', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_department')
    designation = models.ForeignKey('master.Designation', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_designation')
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_manager')
    hire_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    employee_type = models.CharField(max_length=10, choices=EmployeeType.choices, default=EmployeeType.FULL)
    work_schedule = models.CharField(max_length=10, choices=WorkSchedule.choices, default=WorkSchedule.EIGHT_HOURS)
    visa_status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='employees_photos/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    is_training_completed = models.BooleanField(default=False)
    willing_to_travel = models.BooleanField(default=False)
    badge = models.CharField(max_length=10, choices=EmployeeBadge.choices, default=EmployeeBadge.SILVER)
    national_id_type = models.CharField(max_length=10, choices=NationalIDType.choices, default=NationalIDType.AADHAR)
    national_id_no = models.TextField(default='NA')
    national_id_image = models.ImageField(upload_to='employees_national_id/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    PAN_no = models.TextField(default='NA')
    PAN_image = models.ImageField(upload_to='employees_pan/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    passport_no = models.TextField(default='NA')
    passport_image = models.ImageField(upload_to='employees_passports/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    passport_issue_date = models.DateField(null=True, blank=True)
    passport_expiry_date = models.DateField(null=True, blank=True)
    passport_issue_country = models.ForeignKey('master.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_passport_issue_country')
    passport_issue_state = models.ForeignKey('master.State', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_passport_issue_state')
    passport_issue_city = models.ForeignKey('master.City', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_passport_issue_city')
    driving_license_no = models.TextField(default='NA')
    driving_license_image = models.ImageField(upload_to='employees_driving_license/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    utility_bill_image = models.ImageField(upload_to='employees_utility_bills/', max_length=200, null=True, blank=True, validators=[validate_image_size_2mb])
    bank_country = models.ForeignKey('master.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_bank_country')
    bank = models.ForeignKey('master.Bank', null=True, blank=True, on_delete=models.SET_NULL, related_name='employees_bank')
    bank_ac_name = models.TextField(default='NA')
    bank_ac_type = models.TextField(default='NA')
    bank_ac_no = models.TextField(default='NA')
    bank_ac_IFSC = models.TextField(default='NA')
    description = models.TextField(default='NA')

    class Meta:
        db_table = '"hr"."employees"'
        indexes = [
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
            models.Index(fields=['department']),
            models.Index(fields=['designation']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_deleted']),
            models.Index(fields=['is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active', 'is_deleted']),
            models.Index(fields=['status', 'is_active']),
            models.Index(fields=['status', 'is_deleted']),
        ]

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

        # If the employee is activated, activate related entities
        if self.is_active:
            if self.city and not self.city.is_active:
                self.city.is_active = True
                self.city.save()

            if self.state and not self.state.is_active:
                self.state.is_active = True
                self.state.save()

            if self.country and not self.country.is_active:
                self.country.is_active = True
                self.country.save()

            if self.department and not self.department.is_active:
                self.department.is_active = True
                self.department.save()

            if self.designation and not self.designation.is_active:
                self.designation.is_active = True
                self.designation.save()

        # If the employee is undeleted, undelete related entities
        if not self.is_deleted:
            if self.city and self.city.is_deleted:
                self.city.is_deleted = False
                self.city.save()

            if self.state and self.state.is_deleted:
                self.state.is_deleted = False
                self.state.save()

            if self.country and self.country.is_deleted:
                self.country.is_deleted = False
                self.country.save()

            if self.department and self.department.is_deleted:
                self.department.is_deleted = False
                self.department.save()

            if self.designation and self.designation.is_deleted:
                self.designation.is_deleted = False
                self.designation.save()

        # Check if is_active has changed
        if not self.is_active:
            # Implement further actions as needed
            pass

        if not self.is_deleted:
            # Implement further actions as needed
            pass

    def __str__(self):
        return self.first_name + ' ' + self.last_name
