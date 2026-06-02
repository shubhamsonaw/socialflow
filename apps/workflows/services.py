from .models import WorkflowStep


class WorkflowEngine:

    @staticmethod
    def complete_step(step):
        step.status = "completed"
        step.save()

        next_step = WorkflowStep.objects.filter(
            task=step.task,
            order=step.order + 1
        ).first()

        if next_step:
            next_step.status = "in_progress"
            next_step.save()

        return next_step