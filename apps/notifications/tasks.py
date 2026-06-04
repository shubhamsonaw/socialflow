from celery import shared_task


@shared_task
def test_notification_task():

    print("Notification task executed")

    return "Success"