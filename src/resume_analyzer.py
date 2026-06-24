from src.keyword_matcher import extract_keywords

def get_resume_stats(resume_text):

    words = len(resume_text.split())
    characters = len(resume_text)
    skills_found = len(extract_keywords(resume_text))

    if words < 200:
        strength = "Weak"
    elif words < 500:
        strength = "Average"
    else:
        strength = "Strong"

    return {
        "words": words,
        "characters": characters,
        "skills": skills_found,
        "strength": strength
    }