def detect_resume_sections(resume_text):

    text = resume_text.lower()

    sections = {
        "Skills": False,
        "Experience": False,
        "Education": False,
        "Projects": False,
        "Certifications": False
    }

    skills_keywords = [
        "skills",
        "technical skills",
        "core competencies"
    ]

    experience_keywords = [
        "experience",
        "work experience",
        "employment",
        "professional experience"
    ]

    education_keywords = [
        "education",
        "academic background",
        "qualification"
    ]

    project_keywords = [
        "projects",
        "project"
    ]

    certification_keywords = [
        "certifications",
        "certificates",
        "certification"
    ]

    for keyword in skills_keywords:
        if keyword in text:
            sections["Skills"] = True

    for keyword in experience_keywords:
        if keyword in text:
            sections["Experience"] = True

    for keyword in education_keywords:
        if keyword in text:
            sections["Education"] = True

    for keyword in project_keywords:
        if keyword in text:
            sections["Projects"] = True

    for keyword in certification_keywords:
        if keyword in text:
            sections["Certifications"] = True

    return sections