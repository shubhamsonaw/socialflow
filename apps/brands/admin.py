from django.contrib import admin
from .models import BrandProfile
# Register your models here.



@admin.register(BrandProfile)
class BrandProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand_name",
        "workspace",
        "tone",
        "audience",
        "created_at",
    )

    search_fields = (
        "brand_name",
        "tone",
        "audience",
    )

    list_filter = (
        "tone",
        "created_at",
    )