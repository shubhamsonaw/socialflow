from django.contrib import admin

# Register your models here.

from .models import Workspace, WorkspaceMember


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    
@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "workspace",
        "user",
        "role",
        "created_at",
    )

    list_filter = (
        "role",
        "workspace",
    )

    search_fields = (
        "user__username",
        "workspace__name",
    )