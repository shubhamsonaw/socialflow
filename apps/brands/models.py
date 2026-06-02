from django.db import models

# Create your models here.


class BrandProfile(models.Model):
    workspace = models.OneToOneField(
        "workspaces.Workspace",
        on_delete=models.CASCADE,
        related_name="brand_profile"
    )

    brand_name = models.CharField(max_length=255)

    tone = models.CharField(
        max_length=100,
        blank=True
    )

    audience = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name