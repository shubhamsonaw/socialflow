from .models import WorkflowStep, ActivityLog


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
        step.save()

        next_step = WorkflowStep.objects.filter(
            task=step.task,
            order=step.order + 1
        ).first()

        if next_step:
            next_step.status = "in_progress"
            next_step.save()

        return next_step