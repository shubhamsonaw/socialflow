from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ScrapeURLSerializer
from .tasks import scrape_website
from .mongo import scraped_pages
from bson import ObjectId
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
        
class ScrapeResultsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        results = []

        for doc in scraped_pages.find().sort("_id", -1):

            results.append({
                "id": str(doc["_id"]),
                "url": doc["url"],
                "status_code": doc["status_code"],
                "scraped_at": str(doc["scraped_at"]),
                "title": doc.get("title", ""),
                "content_preview": doc.get("content_preview", ""),
                "links_count": doc.get("links_count", 0),
            })

        return Response(results)