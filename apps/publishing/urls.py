from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import ScheduledPostViewSet

router = DefaultRouter()
router.register(r"scheduled-posts",ScheduledPostViewSet,basename="scheduled-post")

urlpatterns = router.urls