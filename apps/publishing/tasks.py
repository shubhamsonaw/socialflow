from celery import shared_task
from django.utils import timezone

from .models import ScheduledPost


@shared_task
def publish_scheduled_posts():

    posts = ScheduledPost.objects.filter(
        status="scheduled",
        scheduled_for__lte=timezone.now()
    )

    for post in posts:
        post.status = "published"
        post.published_at = timezone.now()
        post.save()

    return f"{posts.count()} posts published"