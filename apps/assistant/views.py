from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ChatSerializer
from .services import AssistantService

# Create your views here.

class AssistantChatView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ChatMessage.objects.filter(
        user=self.request.user
    )

    def post(self, request):

        serializer = ChatSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        response_text = AssistantService.chat(
            request.user,
            serializer.validated_data["message"]
        )

        return Response({
            "response": response_text
        })
