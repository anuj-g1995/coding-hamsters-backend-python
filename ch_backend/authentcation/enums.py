from django.db import models

class Gender(models.TextChoices):
    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"
class UserState(models.TextChoices):
    VERIFY = "verify"
    STARTED = "started"
    PENDING = "pending"
    VERIFIED = "verified"

class UserType(models.TextChoices):
    PROVIDER = "provider"
    SEEKER = "seeker"

# Can be used in package category's. Currently no where used.
# class PackageCategoryTypes(models.TextChoices):
#     PACEMAKER_ASSISTANCE = 'pacemaker assistance'
#     CHRONIC_DISEASE_MANAGEMENT = 'chronic disease management'
#     ELDERLY_CARE = 'elderly care'
#     POST_OPERATIVE_CARE = 'post operative care'
#     MATERNITY_CARE = 'maternity care'
#     HOME_HEALTHCARE = 'home healthcare'