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

        previous_messages = ChatMessage.objects.filter(
            user=user
        ).order_by("-created_at")[:10]

        context = ""

        for msg in reversed(previous_messages):
            context += f"{msg.role}: {msg.content}\n"

        prompt = f"""
        Conversation History:

        {context}

        Current User Message:
        {message}
        """

        response = GeminiClient.generate_response(
            prompt
        )
        

        ChatMessage.objects.create(
            user=user,
            role="assistant",
            content=response
        )

        return response