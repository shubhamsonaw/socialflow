from django.shortcuts import render
from rest_framework.routers import DefaultRouter

from .views import ContentAnalyticsViewSet


router = DefaultRouter()

router.register("analytics",ContentAnalyticsViewSet)

urlpatterns = router.urls