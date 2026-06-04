from django.db import models

# Create your models here.

class ContentAnalytics(models.Model):
    platform = models.CharField(max_length=50)

    content_title = models.CharField(max_length=255)

    impressions = models.IntegerField(default=0)

    likes = models.IntegerField(default=0)

    comments = models.IntegerField(default=0)

    shares = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_title