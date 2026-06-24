from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    final_score,
    match_score,
    structure_score,
    strength_score,
    matched_keywords,
    missing_keywords,
    sections,
    ai_review=None
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "AI Resume ATS Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    # Scores
    elements.append(
        Paragraph(
            f"<b>Final ATS Score:</b> {final_score}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Keyword Match Score:</b> {match_score}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Structure Score:</b> {structure_score}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Strength Score:</b> {strength_score}%",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 12))

    # Structure Analysis
    elements.append(
        Paragraph(
            "Resume Structure Analysis",
            styles["Heading2"]
        )
    )

    for section, found in sections.items():

        status = "Found" if found else "Missing"

        elements.append(
            Paragraph(
                f"{section}: {status}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 12))

    # Matched Keywords
    elements.append(
        Paragraph(
            "Matched Keywords",
            styles["Heading2"]
        )
    )

    for keyword in matched_keywords:

        elements.append(
            Paragraph(
                f"• {keyword}",
                styles["Normal"]
            )
        )

    elements.append(Spacer(1, 12))

    # Missing Keywords
    elements.append(
        Paragraph(
            "Missing Keywords",
            styles["Heading2"]
        )
    )

    for keyword in missing_keywords:

        elements.append(
            Paragraph(
                f"• {keyword}",
                styles["Normal"]
            )
        )

    # AI Review
    if ai_review:

        elements.append(PageBreak())

        elements.append(
            Paragraph(
                "AI Resume Review",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                ai_review,
                styles["Normal"]
            )
        )

    doc.build(elements)