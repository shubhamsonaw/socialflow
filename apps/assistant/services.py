from .models import ChatMessage
from .llm_client import GeminiClient
from apps.brands.models import BrandProfile
from .intent_router import IntentRouter
from .prompt_templates import PromptTemplates


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
            
        brand = BrandProfile.objects.filter(
            workspace=user.workspace
        ).first()

        brand_context = ""

        if brand:
            brand_context = f"""
        Brand Name: {brand.brand_name}
        Tone: {brand.tone}
        Audience: {brand.audience}
        """

        intent = IntentRouter.detect_intent(
            message
        )
        
        if intent == "generate_post":

            topic = IntentRouter.extract_topic(
                message
            )
            
            prompt = PromptTemplates.generate_post(
                topic=topic,
                brand_name=brand.brand_name if brand else "Generic Brand",
                tone=brand.tone if brand else "Professional",
                audience=brand.audience if brand else "General Audience",
            )

        elif intent == "improve_post":

            prompt = PromptTemplates.improve_post(
                message
            )

        elif intent == "content_ideas":

            prompt = PromptTemplates.generate_content_ideas(
                brand_name=brand.brand_name if brand else "Generic Brand",
                tone=brand.tone if brand else "Professional",
                audience=brand.audience if brand else "General Audience",
            )

        elif intent == "summarize_article":

            prompt = PromptTemplates.summarize_article(
                message
            )

        else:

            prompt = f"""
            You are an AI Social Media Assistant.

            Brand Context:
            {brand_context}

            Conversation History:
            {context}

            Current User Message:
            {message}

            Generate content matching the brand voice,
            tone, and target audience.
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
    

    
    