import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

with open("transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

prompt = f"""
You are an expert video summarization assistant.

Summarize the following YouTube video transcript.

Give the response in this structure:

## Summary
Write a clear 1-2 paragraph summary.

## Key Points
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

## Technical Concepts
List the important technical concepts discussed.

Transcript:
{transcript}
"""

response = client.models.generate_content(
    # model="gemini-2.5-flash",
    model="gemini-3.6-flash",
    contents=prompt
)

print("\n========== GEMINI SUMMARY ==========\n")
print(response.text)