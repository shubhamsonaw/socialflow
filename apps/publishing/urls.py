from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import ScheduledPostViewSet

from django.urls import path
from .views import LinkedInConnectView

router = DefaultRouter()
router.register(
    r"scheduled-posts",
    ScheduledPostViewSet,
    basename="scheduled-post"
)

urlpatterns = [
    path("linkedin/connect/",LinkedInConnectView.as_view(),name="linkedin-connect"),
    
]

urlpatterns += router.urls