from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import ReportService
# Create your views here.

class ReportSummaryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        report = ReportService.generate_summary(
            request.user.workspace
        )

        return Response(report)