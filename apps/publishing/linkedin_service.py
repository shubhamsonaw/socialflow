from django.conf import settings


class LinkedInService:

    @staticmethod
    def get_authorization_url():
        return (
            "https://www.linkedin.com/oauth/v2/authorization"
        )