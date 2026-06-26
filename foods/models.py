from django.db import models
from vendors.models import Vendor

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class FoodItem(models.Model):

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='foods'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="foods/"
    )

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    