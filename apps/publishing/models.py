from django.db import models
from django.conf import settings
# Create your models here.

class ScheduledPost(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("published", "Published"),
        ("failed", "Failed"),
    )

    PLATFORM_CHOICES = (
        ("linkedin", "LinkedIn"),
        ("twitter", "Twitter/X"),
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
    )

    workspace = models.ForeignKey(
        "workspaces.Workspace",
        on_delete=models.CASCADE,
        related_name="scheduled_posts"
    )

    brand = models.ForeignKey(
        "brands.BrandProfile",
        on_delete=models.CASCADE,
        related_name="scheduled_posts"
    )

    content = models.TextField()

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    scheduled_for = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.platform} - {self.status}"
    
class SocialAccount(models.Model):
    class SocialAccount(models.Model):
        PLATFORM_CHOICES = (
            ("linkedin", "LinkedIn"),
            ("twitter", "Twitter/X"),
            ("facebook", "Facebook"),
            ("instagram", "Instagram"),
        )

        workspace = models.ForeignKey(
            "workspaces.Workspace",
            on_delete=models.CASCADE,
            related_name="social_accounts"
        )

        platform = models.CharField(
            max_length=20,
            choices=PLATFORM_CHOICES
        )

        account_name = models.CharField(
            max_length=255
        )

        access_token = models.TextField()

        is_active = models.BooleanField(
            default=True
        )

        connected_at = models.DateTimeField(
            auto_now_add=True
        )

        def __str__(self):
            return f"{self.account_name} ({self.platform})"