from django.contrib import admin
from .models import ContentAnalytics
# Register your models here.

@admin.register(ContentAnalytics)
class ContentAnalyticsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_title",
        "platform",
        "impressions",
        "likes",
        "comments",
        "shares",
    )