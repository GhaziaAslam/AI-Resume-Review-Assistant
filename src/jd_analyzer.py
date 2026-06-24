import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_job_skills(job_description):

    prompt = f"""
You are an ATS Skill Extraction Engine.

Extract the important skills, tools, technologies,
soft skills, certifications and qualifications
from the job description.

Return ONLY a Python list.

Example:

["Python", "SQL", "Leadership", "Communication"]

Job Description:

{job_description}
"""

    try:

        model = genai.GenerativeModel(
            "gemini-flash-latest"
        )

        response = model.generate_content(
            prompt
        )

        skills_text = response.text.strip()

        skills_text = skills_text.replace(
            "```python",
            ""
        )

        skills_text = skills_text.replace(
            "```",
            ""
        )

        skills = eval(skills_text)

        return [
            skill.lower()
            for skill in skills
        ]

    except Exception as e:

        print("ERROR:", e)

        return []


if __name__ == "__main__":

    jd = """
    We are looking for a Sales Manager with experience in CRM,
    Lead Generation, Negotiation, Team Management,
    Communication Skills and Microsoft Excel.
    """

    skills = extract_job_skills(jd)

    print(skills)