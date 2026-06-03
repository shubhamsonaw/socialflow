from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import WorkflowTaskViewSet
from .views import  WorkflowStepViewSet

router = DefaultRouter()
router.register("tasks",WorkflowTaskViewSet,basename="workflow-task")
urlpatterns = router.urls

router.register("workflow-steps",WorkflowStepViewSet,basename="workflow-step")
urlpatterns = router.urls