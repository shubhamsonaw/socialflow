from rest_framework import serializers
from .models import WorkflowTask
from .models import WorkflowTask, WorkflowStep
from rest_framework import serializers
from .models import WorkflowRule


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
        
class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = "__all__"
        
class WorkflowRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowRule
        fields = "__all__"
        read_only_fields = ("workspace",)