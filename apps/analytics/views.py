from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ContentAnalytics
from .serializers import ContentAnalyticsSerializer
from .services import AnalyticsService

# Create your views here.

class ContentAnalyticsViewSet(viewsets.ModelViewSet):

    queryset = ContentAnalytics.objects.all()

    serializer_class = ContentAnalyticsSerializer

    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        return ContentAnalytics.objects.filter(
        workspace=self.request.user.workspace
    )
        
    def perform_create(self, serializer):
        serializer.save(
        workspace=self.request.user.workspace
        )
    
    @action(
    detail=False,
    methods=["get"]
)
    def top_content(self, request):

        content = AnalyticsService.get_top_content()

        if not content:
            return Response(
                {"message": "No content found"}
            )

        return Response({
            "title": content.content_title,
            "platform": content.platform,
            "engagement_rate": content.engagement_rate
        })