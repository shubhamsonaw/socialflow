from django.contrib import admin
from .models import ScheduledPost, SocialAccount
# Register your models here.

@admin.register(ScheduledPost)
class ScheduledPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "platform",
        "status",
        "scheduled_for",
        "published_at",
    )

    list_filter = (
        "platform",
        "status",
    )

    search_fields = (
        "content",
    )


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "account_name",
        "platform",
        "workspace",
        "is_active",
        "connected_at",
    )

    list_filter = (
        "platform",
        "is_active",
    )

    search_fields = (
        "account_name",
    )