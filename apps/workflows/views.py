from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkflowTask
from .serializers import WorkflowTaskSerializer
from rest_framework.permissions import IsAuthenticated

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