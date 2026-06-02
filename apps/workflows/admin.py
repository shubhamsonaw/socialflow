from django.contrib import admin
from .models import WorkflowTask
from .models import WorkflowTask, WorkflowStep, ActivityLog
# Register your models here.

@admin.register(WorkflowTask)
class WorkflowTaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "status",
        "priority",
        "created_at",
    )
    
@admin.register(WorkflowStep)
class WorkflowStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "name",
        "order",
        "status",
    )
    
@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "user",
        "action",
        "created_at"
    )