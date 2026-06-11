from django.contrib import admin
from .models import WorkflowTask
from .models import WorkflowTask, WorkflowStep, ActivityLog, WorkflowRule
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
    
@admin.register(WorkflowRule)
class WorkflowRuleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "trigger",
        "action",
        "workspace",
        "is_active",
        "created_at",
    )

    list_filter = (
        "trigger",
        "action",
        "is_active",
    )

    search_fields = (
        "name",
    )