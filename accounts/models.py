from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    REEL_CHOICES = (
        ('customer','Customer'),
        ('vendor','Vendor'),
        ('admin', 'Admin'),
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=REEL_CHOICES, default='customer')



    def __str__(self):
        return self.username
    