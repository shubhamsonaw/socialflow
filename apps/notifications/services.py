from .models import Notification


class NotificationService:

    @staticmethod
    def create_notification(
        user,
        title,
        message
    ):

        return Notification.objects.create(
            user=user,
            title=title,
            message=message
        )