from django.db import models
from django.conf import settings
# Create your models here.

class Vendor(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    shop_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    description = models.CharField(
        blank=True,
        null=True
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.shop_name
    