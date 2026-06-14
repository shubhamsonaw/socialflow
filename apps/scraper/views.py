from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ScrapeURLSerializer
from .tasks import scrape_website
# Create your views here.

class ScrapeWebsiteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ScrapeURLSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        url = serializer.validated_data["url"]

        scrape_website.delay(url)

        return Response({
            "message": "Scraping started",
            "url": url
        })