from apps.publishing.models import ScheduledPost
from apps.notifications.models import Notification
from apps.analytics.models import ContentAnalytics
from apps.workflows.models import (
    WorkflowTask,
    WorkflowRule,
)


class DashboardService:

    @staticmethod
    def get_workspace_summary(workspace, user):

        analytics = ContentAnalytics.objects.filter(
            workspace=workspace
        )

        return {
            "workspace_name": workspace.name,

            "posts": {
                "total": ScheduledPost.objects.filter(
                    workspace=workspace
                ).count(),

                "draft": ScheduledPost.objects.filter(
                    workspace=workspace,
                    status="draft"
                ).count(),

                "scheduled": ScheduledPost.objects.filter(
                    workspace=workspace,
                    status="scheduled"
                ).count(),

                "published": ScheduledPost.objects.filter(
                    workspace=workspace,
                    status="published"
                ).count(),
            },

            "notifications": {
                "total": Notification.objects.filter(
                    user=user
                ).count(),

                "unread": Notification.objects.filter(
                    user=user,
                    is_read=False
                ).count(),
            },

            "tasks": {
                "total": WorkflowTask.objects.filter(
                    workspace=workspace
                ).count(),

                "pending": WorkflowTask.objects.filter(
                    workspace=workspace,
                    status="pending"
                ).count(),

                "completed": WorkflowTask.objects.filter(
                    workspace=workspace,
                    status="completed"
                ).count(),
            },

            "workflow_rules": {
                "total": WorkflowRule.objects.filter(
                    workspace=workspace
                ).count(),

                "active": WorkflowRule.objects.filter(
                    workspace=workspace,
                    is_active=True
                ).count(),
            },

            "analytics": {
                "total_records": analytics.count(),

                "total_impressions":
                    sum(a.impressions for a in analytics),

                "total_likes":
                    sum(a.likes for a in analytics),

                "total_comments":
                    sum(a.comments for a in analytics),

                "total_shares":
                    sum(a.shares for a in analytics),
            }
        }