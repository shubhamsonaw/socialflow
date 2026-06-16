from .llm_client import GeminiClient
from .prompt_templates import GENERATE_POST_PROMPT


def generate_post(topic):

    prompt = GENERATE_POST_PROMPT.format(
        topic=topic
    )

    return GeminiClient.generate_response(
        prompt
    )