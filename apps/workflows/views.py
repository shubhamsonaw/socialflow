from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkflowTask
from .serializers import WorkflowTaskSerializer, WorkflowStepSerializer
from rest_framework.permissions import IsAuthenticated
from .models import WorkflowTask, WorkflowStep
from .services import WorkflowEngine
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

# class WorkflowTaskViewSet(viewsets.ModelViewSet):
#     queryset = WorkflowTask.objects.all()
#     serializer_class = WorkflowTaskSerializer
#     permission_classes = [IsAuthenticated]

class WorkflowTaskViewSet(viewsets.ModelViewSet):
    queryset = WorkflowTask.objects.all()
    serializer_class = WorkflowTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkflowTask.objects.filter(
            workspace=self.request.user.workspace
        )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            workspace=self.request.user.workspace
        )
        
class WorkflowStepViewSet(viewsets.ModelViewSet):

    queryset = WorkflowStep.objects.all()
    serializer_class = WorkflowStepSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):

        step = self.get_object()

        next_step = WorkflowEngine.complete_step(step)

        return Response({
            "message": "Step completed successfully",
            "next_step": next_step.name if next_step else None
        })