from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ScheduledPost
from .serializers import ScheduledPostSerializer

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .linkedin_service import LinkedInService

# Create your views here.

class ScheduledPostViewSet(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = [IsAuthenticated]
    
class LinkedInConnectView(APIView):

    def get(self, request):
        auth_url = (
            f"https://www.linkedin.com/oauth/v2/authorization"
            f"?response_type=code"
            f"&client_id={settings.LINKEDIN_CLIENT_ID}"
            f"&redirect_uri={settings.LINKEDIN_REDIRECT_URI}"
            f"&scope=openid%20profile%20email"
        )

        return Response({
            "authorization_url": auth_url
        })