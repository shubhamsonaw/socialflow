from django.db.models import Sum

from apps.analytics.models import ContentAnalytics
from apps.publishing.models import ScheduledPost
from apps.workflows.models import WorkflowTask


class ReportService:

    @staticmethod
    def generate_summary(workspace):

        analytics = ContentAnalytics.objects.filter(
            workspace=workspace
        )

        posts = ScheduledPost.objects.filter(
            workspace=workspace
        )

        tasks = WorkflowTask.objects.filter(
            workspace=workspace
        )

        impressions = analytics.aggregate(
            total=Sum("impressions")
        )["total"] or 0

        likes = analytics.aggregate(
            total=Sum("likes")
        )["total"] or 0

        comments = analytics.aggregate(
            total=Sum("comments")
        )["total"] or 0

        shares = analytics.aggregate(
            total=Sum("shares")
        )["total"] or 0

        engagement_rate = 0

        if impressions > 0:
            engagement_rate = round(
                ((likes + comments + shares) / impressions) * 100,
                2
            )

        return {
            "workspace": workspace.name,

            "analytics": {
                "impressions": impressions,
                "likes": likes,
                "comments": comments,
                "shares": shares,
                "engagement_rate": engagement_rate,
            },

            "publishing": {
                "total_posts": posts.count(),
                "published_posts": posts.filter(
                    status="published"
                ).count(),
            },

            "workflow": {
                "total_tasks": tasks.count(),
                "completed_tasks": tasks.filter(
                    status="completed"
                ).count(),
            }
        }