from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import WorkflowTaskViewSet

router = DefaultRouter()
router.register("tasks", WorkflowTaskViewSet)

urlpatterns = router.urls