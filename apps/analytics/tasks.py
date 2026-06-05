from celery import shared_task
from apps.notifications.services import NotificationService
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def generate_daily_report():
    users = User.objects.all()

    for user in users:
        NotificationService.create_notification(
            user=user,
            title="Daily Analytics Report",
            message="Your daily analytics report is ready."
        )

    return "Daily reports generated"