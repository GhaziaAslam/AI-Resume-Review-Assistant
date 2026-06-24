from src.jd_analyzer import extract_job_skills

jd = """
We are looking for a Sales Manager with experience in CRM,
Lead Generation, Negotiation, Team Management,
Communication Skills and Microsoft Excel.
"""

skills = extract_job_skills(jd)

print(skills)