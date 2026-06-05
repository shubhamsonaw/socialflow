from .models import WorkflowStep, ActivityLog
from apps.notifications.services import NotificationService
from apps.notifications.tasks import create_notification_task

class WorkflowEngine:

    @staticmethod
    def complete_step(step):
        step.status = "completed"
        step.save()
        
        ActivityLog.objects.create(
            task=step.task,
            user=step.task.created_by,
            action="step_completed",
            description=f"{step.name} completed"
        )
        # step.save()
        
        create_notification_task.delay(
            step.task.created_by.id,
            "Workflow Update",
            f"{step.name} completed successfully"
            )


        next_step = WorkflowStep.objects.filter(
            task=step.task,
            order=step.order + 1
        ).first()

        if next_step:
            next_step.status = "in_progress"
            next_step.save()

        return next_step
    
       