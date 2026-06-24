SKILL_GUIDE = {
    "aws": "Learn AWS Cloud Fundamentals",
    "docker": "Learn Docker & Containers",
    "kubernetes": "Learn Kubernetes Basics",
    "sql": "Practice SQL Queries",
    "python": "Build Python Projects",
}

def get_skill_recommendations(missing_keywords):
    recommendations = []

    for skill in missing_keywords:
        key = skill.lower()

        if key in SKILL_GUIDE:
            recommendations.append(
                SKILL_GUIDE[key]
            )

    return recommendations