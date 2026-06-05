# from celery import shared_task


# @shared_task
# def test_notification_task():

#     print("Notification task executed")

#     return "Success"

from celery import shared_task
from .models import Notification
from apps.accounts.models import User


@shared_task
def create_notification_task(
    user_id,
    title,
    message
):
    user = User.objects.get(id=user_id)

    Notification.objects.create(
        user=user,
        title=title,
        message=message
    )

    return "Notification Created"