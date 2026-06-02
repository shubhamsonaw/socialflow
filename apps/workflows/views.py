from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkflowTask
from .serializers import WorkflowTaskSerializer

# Create your views here.

class WorkflowTaskViewSet(viewsets.ModelViewSet):
    queryset = WorkflowTask.objects.all()
    serializer_class = WorkflowTaskSerializer