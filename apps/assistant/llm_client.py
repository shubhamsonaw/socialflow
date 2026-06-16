# import google.generativeai as genai

# from django.conf import settings


# genai.configure(
#     api_key=settings.GEMINI_API_KEY
# )


# class GeminiClient:

#     @staticmethod
#     def generate_response(prompt):

#         model = genai.GenerativeModel("gemini-2.5-flash")

#         response = model.generate_content(
#             prompt
#         )

#         return response.text


from google import genai

from django.conf import settings


class GeminiClient:

    @staticmethod
    def generate_response(prompt):

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text