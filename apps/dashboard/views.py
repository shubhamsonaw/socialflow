from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services import DashboardService

# Create your views here.



class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = DashboardService.get_workspace_summary(
            workspace=request.user.workspace,
            user=request.user
        )

        return Response(data)