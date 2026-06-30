from django.contrib import admin
from .models import Reel


@admin.register(Reel)
class ReelAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "vendor",
        "food",
        "created_at",
        "is_active",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "caption",
    )