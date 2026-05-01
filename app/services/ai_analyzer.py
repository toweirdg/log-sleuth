import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_log_with_ai(message: str, category: str, pattern):

    prompt = f"""
You are a senior DevOps engineer.

Analyze this log and provide:

1. Root cause
2. Severity (Low/Medium/High)
3. Suggested fix

Log: {message}
Category: {category}
Pattern: {pattern}

Return JSON format:
{{
	"root_cause": "...",
	"severity": "...",
	"suggestion": "..."
}}
"""

    response = client.chat.completions.create(
        model="gpt-40-mini",
        messages=[
            {"role": "system", "content": "You analyze system logs."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
