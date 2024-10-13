# utils/enums.py

from django.db import models
from django.utils.translation import gettext_lazy as _

# Status Type Enum
class StatusType(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    REVIEW = 'review', _('Review')
    PUBLISHED = 'published', _('Published')

# Designation Level Enum
class DesignationLevel(models.TextChoices):
    ENTRY = 'entry', _('Entry')
    MID = 'mid', _('Mid')
    SENIOR = 'senior', _('Senior')
    EXECUTIVE = 'exe', _('Executive')
    OTHER = 'other', _('Other')

# Employee Type Enum
class EmployeeType(models.TextChoices):
    FULL = 'full', _('Full-time')
    PART = 'part', _('Part-time')
    CONTRACT = 'contract', _('Contract')

# Employee Badge Enum
class EmployeeBadge(models.TextChoices):
    SILVER = 'silver', _('Silver')
    GOLD = 'gold', _('Gold')
    DIAMOND = 'diamond', _('Diamond')

# Work Schedule Enum
class WorkSchedule(models.TextChoices):
    FOUR_HOURS = '4hr', _('4 Hours')
    SIX_HOURS = '6hr', _('6 Hours')
    EIGHT_HOURS = '8hr', _('8 Hours')

# National ID Type Enum
class NationalIDType(models.TextChoices):
    SSN = 'SSN', _('Social Security Number (SSN)')
    NIN = 'NIN', _('National Insurance Number (NIN)')
    AADHAR = 'Aadhar', _('Aadhar')
    PAN = 'PAN', _('PAN')