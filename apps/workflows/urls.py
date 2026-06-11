from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import WorkflowTaskViewSet
from .views import  WorkflowStepViewSet
from .views import WorkflowRuleViewSet

router = DefaultRouter()

router.register("tasks",WorkflowTaskViewSet,basename="workflow-task")
router.register("workflow-steps",WorkflowStepViewSet,basename="workflow-step")
router.register("workflow-rules",WorkflowRuleViewSet,basename="workflow-rule")

urlpatterns = router.urls