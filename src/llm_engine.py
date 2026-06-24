import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-flash-latest")


def review_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

1. ATS Match Analysis
2. Missing Skills
3. Resume Improvements
4. Strong Points
5. Final Recommendation

Format the response clearly using headings and bullet points.
"""

    response = model.generate_content(prompt)

    return response.text