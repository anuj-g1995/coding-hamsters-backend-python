from django.utils import timezone


from .enums import Gender
from .enums import UserType
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_role = models.CharField(max_length=20,choices=UserType.choices, blank=True, null=True)
    
    # Add your custom fields here
    USERNAME_FIELD = "email"
    
# class Profile(models.Model):
#     disablity_type = models.CharField(max_length=20,choices=UserType.choices, blank=True, null=True)
#     # product = models.ForeignKey(User)
    
#     # # method for updating@receiver(post_save, sender=TransactionDetail, dispatch_uid="update_stock_count")
#     # def update_stock(sender, instance, **kwargs):
#     #     instance.product.stock -= instance.amount
#     #     instance.product.save()