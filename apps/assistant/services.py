from .models import ChatMessage
from .llm_client import GeminiClient


class AssistantService:

    @staticmethod
    def chat(user, message):

        ChatMessage.objects.create(
            user=user,
            role="user",
            content=message
        )

        response = GeminiClient.generate_response(
            message
        )

        ChatMessage.objects.create(
            user=user,
            role="assistant",
            content=response
        )

        return response