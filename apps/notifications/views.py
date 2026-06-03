from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):

    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    @action(detail=True, methods=["post"])
    def read(self, request, pk=None):

        notification = self.get_object()

        notification.is_read = True
        notification.save()

        return Response({
            "message": "Notification marked as read"
        })