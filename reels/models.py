from django.db import models
from django.conf import settings
from vendors.models import Vendor
from foods.models import FoodItem




class Reel(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )

    food = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=150)
    video = models.FileField(upload_to="reels/")

    thumbnail = models.ImageField(
        upload_to="reel_thumbnail/",
        blank=True,
        null=True
    )

    caption = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-created_at"]


    def __str__(self):
        return self.title
    


    
