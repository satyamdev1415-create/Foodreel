from django.db import models
from django.conf import settings
from foods.models import FoodItem
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ("user","food")

    def total_price(self):
        return self.food.price * self.quantity


    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
    