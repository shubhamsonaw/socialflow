from .models import WorkspaceMember


def is_workspace_admin(user):
    return WorkspaceMember.objects.filter(
        user=user,
        role="ADMIN"
    ).exists()


def is_workspace_manager(user):
    return WorkspaceMember.objects.filter(
        user=user,
        role__in=["ADMIN", "MANAGER"]
    ).exists()