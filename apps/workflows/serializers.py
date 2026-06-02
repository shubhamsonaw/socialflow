from rest_framework import serializers
from .models import WorkflowTask


class WorkflowTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowTask
        fields = "__all__"
        
        read_only_fields = (
            "workspace",
            "created_by",
            "created_at",
            "updated_at",
        )