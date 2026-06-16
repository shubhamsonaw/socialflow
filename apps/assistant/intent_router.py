# from .llm_client import GeminiClient
# from .prompt_templates import GENERATE_POST_PROMPT


# def generate_post(topic):

#     prompt = GENERATE_POST_PROMPT.format(
#         topic=topic
#     )

#     return GeminiClient.generate_response(
#         prompt
#     )
    
# class IntentRouter:

#     @staticmethod
#     def handle(intent, data):

#         if intent == "generate_post":

#             prompt = GENERATE_POST_PROMPT.format(
#                 topic=data["topic"]
#             )

#             return GeminiClient.generate_response(
#                 prompt
#             )

#         raise ValueError(
#             f"Unsupported intent: {intent}"
#         )

class IntentRouter:

    @staticmethod
    def detect_intent(message):

        message = message.lower()

        if "create post" in message:
            return "generate_post"

        if "write post" in message:
            return "generate_post"

        if "linkedin post" in message:
            return "generate_post"

        if "improve post" in message:
            return "improve_post"

        if "rewrite post" in message:
            return "improve_post"

        if "content ideas" in message:
            return "content_ideas"

        if "ideas for content" in message:
            return "content_ideas"

        if "summarize article" in message:
            return "summarize_article"

        if "summarize content" in message:
            return "summarize_article"

        return "general_chat"