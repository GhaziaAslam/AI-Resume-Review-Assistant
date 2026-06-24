import re

SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "sql",
    "data analysis",
    "data science",
    "nlp",
    "computer vision",
    "statistics",
    "aws",
    "azure",
    "google cloud",
    "docker",
    "git",
    "java",
    "c++",
    "r",
    "algorithms",
    "research",
    "model deployment",
    "data preprocessing",
    "software engineering",
    "cloud",
    "business analysis",
    "fastapi",
    "flask",
    "streamlit",
    "langchain",
    "llm",
    "rag",
    "vector database",
    "prompt engineering",
    "power bi",
    "excel"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)
    return text

def extract_keywords(text):

    text = clean_text(text)

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return set(found_skills)

def calculate_match_score(resume_text, job_description):

    resume_keywords = extract_keywords(resume_text)

    jd_keywords = extract_keywords(job_description)

    matched_keywords = list(
        resume_keywords.intersection(jd_keywords)
    )

    missing_keywords = list(
        jd_keywords - resume_keywords
    )

    if len(jd_keywords) == 0:
        return 0, [], []

    score = round(
        (len(matched_keywords) / len(jd_keywords)) * 100,
        2
    )

    return score, matched_keywords, missing_keywords
   
def calculate_dynamic_match_score(
    resume_text,
    jd_skills
):

    resume_text = resume_text.lower()

    matched_keywords = []

    missing_keywords = []

    for skill in jd_skills:

        if skill.lower() in resume_text:
            matched_keywords.append(skill)

        else:
            missing_keywords.append(skill)

    if len(jd_skills) == 0:
        return 0, [], []

    score = round(
        (len(matched_keywords) / len(jd_skills)) * 100,
        2
    )

    return (
        score,
        matched_keywords,
        missing_keywords
    )