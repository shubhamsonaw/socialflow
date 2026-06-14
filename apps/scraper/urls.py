from django.urls import path

from .views import ScrapeWebsiteAPIView,ScrapeResultsAPIView

urlpatterns = [
    
    path("scrape/",ScrapeWebsiteAPIView.as_view()),
    path("results/", ScrapeResultsAPIView.as_view()),
    
]