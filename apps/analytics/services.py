from .models import ContentAnalytics


class AnalyticsService:

    @staticmethod
    def get_top_content():

        analytics = ContentAnalytics.objects.all()

        best_post = None
        highest_rate = 0

        for item in analytics:

            if item.engagement_rate > highest_rate:

                highest_rate = item.engagement_rate

                best_post = item

        return best_post