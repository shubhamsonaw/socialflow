from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "role",
                    "workspace",
                )
            },
        ),
    )

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "workspace",
        "is_staff",
    )