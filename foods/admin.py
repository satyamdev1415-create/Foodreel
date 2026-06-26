from django.contrib import admin
from .models import Category, FoodItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "slug",
        "created_at"
    ]

    search_fields = [
        "name"
    ]

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(FoodItem)
class FoodAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "vendor",
        "category",
        "price",
        "is_available"
    ]

    list_filter = [
        "category",
        "is_available"
    ]

    search_fields = [
        "name"
    ]