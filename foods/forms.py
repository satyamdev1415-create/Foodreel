from django import forms
from .models import FoodItem


class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodItem

        fields = [
            'category',
            'name',
            'description',
            'price',
            'image',
            'is_available'
        ]