from django.urls import path

from .views import ScrapeWebsiteAPIView

urlpatterns = [
    
    path("scrape/",ScrapeWebsiteAPIView.as_view()),
    
]