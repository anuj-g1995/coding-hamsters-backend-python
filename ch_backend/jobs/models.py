from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class ApplicationStatus(models.TextChoices):
    REJECTED = "rejected"
    SHORTLISTED = "shortlisted"
    NEW = "new"


class EmployeeType(models.TextChoices):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"


class JobStatus(models.TextChoices):
    ACTIVE = "active"
    EXPIRED = "expired"


class JobCategory(models.TextChoices):
    BLINDNESS = 'Blidness'
    PARTIAL = 'Partial blindness'
    HEARING = 'Hearing'
    IMPAIREMENT = 'Impairement'
    HANDICAP = 'Handicap'
    PERSON_WITH_DISABILITY = 'Person_with_Disability'


class ExperianceLevel(models.TextChoices):
    ONE = "0-1 years"
    ONE_TWO = "1-2 years"
    TWO_THREE = "2-3 years"
    TWO_FIVE = "2-5 years"
    FIVE_TEN = "5-10 years"
    TEN_ABOVE = "10+ years"


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Job(TimeStampedModel):
    company = models.CharField(max_length=100)
    vacancies = models.IntegerField(default=0, null=True, blank=True)
    employee_type = models.CharField(choices=EmployeeType.choices, max_length=50)
    location = models.CharField(max_length=100, null=True, blank=True)
    salary_range = models.CharField(max_length=40,default=0, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    job_title = models.CharField(max_length=30, null=True,blank=True)
    status = models.CharField(choices=JobStatus.choices, default="active", max_length=20)
    expiry_date = models.DateField(default=None,blank=True,null=True)
    experience = models.CharField(choices=ExperianceLevel.choices, default='0-1 years',max_length=50)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=JobCategory.choices, max_length=50, null=True)

    class Meta:
        db_table = 'Job'

    def __str__(self):
        return str(self.company)


class JobApplyModel(TimeStampedModel):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="user")
    jobid = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job")
    hiring_text = models.CharField(max_length=400, default="No Reason")
    application_status = models.CharField(choices=ApplicationStatus.choices, default='new', max_length=50)
    is_applied = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
