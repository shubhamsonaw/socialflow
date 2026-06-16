# GENERATE_POST_PROMPT = """
# You are a professional social media content strategist.

# Create an engaging LinkedIn post about:

# Topic: {topic}

# Requirements:
# - Strong opening hook
# - Clear value
# - Professional tone
# - Call to action
# - 150-250 words
# """

class PromptTemplates:

    @staticmethod
    def generate_post(topic):
        return f"""
You are a professional social media content strategist.

Write an engaging LinkedIn post about:

Topic: {topic}

Requirements:
- Professional tone
- Easy to read
- Hook at the beginning
- Actionable insights
- Call to action at the end
- Add relevant hashtags

Return only the post.
"""

    @staticmethod
    def improve_post(content):
        return f"""
You are a professional social media content editor.

Improve the following post:

{content}

Requirements:
- Improve readability
- Improve engagement
- Improve clarity
- Keep original meaning
- Add strong hook

Return only the improved post.
"""

    @staticmethod
    def generate_content_ideas(
        brand_name,
        tone,
        audience
    ):
        return f"""
You are a social media strategist.

Brand Name:
{brand_name}

Brand Tone:
{tone}

Target Audience:
{audience}

Generate 10 content ideas.

Requirements:
- Practical
- Engaging
- Audience focused
- Easy to create

Return as numbered list.
"""

    @staticmethod
    def summarize_article(content):
        return f"""
You are an expert content analyst.

Analyze the article below:

{content}

Return:

1. Summary
2. Key Insights
3. Content Opportunities
4. Suggested Social Media Post

Keep response concise.
"""