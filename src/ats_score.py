def calculate_final_ats_score(
    match_score,
    sections,
    strength
):

    total_sections = len(sections)

    found_sections = sum(
        sections.values()
    )

    structure_score = round(
        (found_sections / total_sections) * 100,
        2
    )

    strength_map = {
        "Weak": 40,
        "Average": 70,
        "Strong": 100
    }

    strength_score = strength_map.get(
        strength,
        50
    )

    final_score = round(
        (
            match_score * 0.6
            +
            structure_score * 0.2
            +
            strength_score * 0.2
        ),
        2
    )

    return (
        final_score,
        structure_score,
        strength_score
    )