
import streamlit as st

# Session state initialization
if "ai_review" not in st.session_state:
    st.session_state["ai_review"] = "AI Review Not Generated"

# Imports
from src.resume_parser import extract_text_from_pdf
from src.keyword_matcher import calculate_match_score
from src.llm_engine import review_resume
from src.resume_analyzer import get_resume_stats
from src.section_detector import detect_resume_sections
from src.ats_score import calculate_final_ats_score
from src.skill_recommender import get_skill_recommendations
from src.pdf_report import generate_pdf_report

# PDF functions
try:
    from src.pdf_report import generate_pdf_report, generate_report
except ImportError:
    generate_pdf_report = None
    generate_report = None

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="AI Resume Review Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Review Assistant")

st.markdown(
    "Upload your resume and compare it with a job description to check ATS compatibility."
)

# ---------------------------
# Inputs
# ---------------------------

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# ---------------------------
# Main App
# ---------------------------

if uploaded_resume:

    try:

        resume_text = extract_text_from_pdf(uploaded_resume)

        sections = detect_resume_sections(resume_text)

        st.success("✅ Resume uploaded successfully!")

        # Resume Structure
        st.subheader("📑 Resume Structure Analysis")

        for section, found in sections.items():
            if found:
                st.success(f"✅ {section} Found")
            else:
                st.error(f"❌ {section} Missing")

        # Resume Stats
        stats = get_resume_stats(resume_text)

        st.subheader("📈 Resume Statistics")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Words", stats.get("words", 0))

        with c2:
            st.metric("Characters", stats.get("characters", 0))

        with c3:
            st.metric("Skills Found", stats.get("skills", 0))

        st.metric(
            "Resume Strength",
            stats.get("strength", 0)
        )

        # Length Check
        words = stats.get("words", 0)

        if words < 250:
            st.warning("⚠️ Resume may be too short.")
        elif words > 1200:
            st.warning("⚠️ Resume may be too long.")

        # Resume Preview
        with st.expander("View Extracted Resume Text"):
            st.text_area(
                "Resume Content",
                resume_text,
                height=300
            )

        # ATS Analysis
        if job_description:

            score, matched_keywords, missing_keywords = (
                calculate_match_score(
                    resume_text,
                    job_description
                )
            )

            final_score, structure_score, strength_score = (
                calculate_final_ats_score(
                    score,
                    sections,
                    stats.get("strength", 0)
                )
            )

            st.subheader("🚀 Professional ATS Score")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Final ATS Score",
                    f"{final_score}%"
                )

            with c2:
                st.metric(
                    "Structure Score",
                    f"{structure_score}%"
                )

            with c3:
                st.metric(
                    "Strength Score",
                    f"{strength_score}%"
                )

            st.progress(
                max(0, min(final_score, 100)) / 100
            )

            if final_score >= 80:
                st.success("🏆 Excellent ATS Profile")
            elif final_score >= 60:
                st.warning("👍 Good ATS Profile")
            else:
                st.error("⚠️ ATS Profile Needs Improvement")

            # ATS Report
            if generate_report:

                if st.button("📥 Generate ATS Report"):

                    try:
                        generate_report(
                            "ats_report.pdf",
                            final_score
                        )

                        with open(
                            "ats_report.pdf",
                            "rb"
                        ) as file:

                            st.download_button(
                                "⬇ Download Report",
                                file,
                                file_name="ATS_Report.pdf",
                                mime="application/pdf"
                            )

                    except Exception as e:
                        st.error(str(e))

            # Matched Keywords
            st.subheader("✅ Matched Keywords")

            if matched_keywords:
                for keyword in matched_keywords:
                    st.write(f"• {keyword}")
            else:
                st.info("No matched keywords found.")

            # Missing Keywords
            st.subheader("💡 Missing Keywords")

            if missing_keywords:
                for keyword in missing_keywords:
                    st.warning(keyword)
            else:
                st.success(
                    "🎉 Great! Your resume matches all detected keywords."
                )

            # Recommendations
            recommendations = get_skill_recommendations(
                missing_keywords
            )

            if recommendations:

                st.subheader(
                    "🎯 Recommended Learning Path"
                )

                for item in recommendations:
                    st.info(item)

            # ATS Feedback
            st.subheader("📝 ATS Feedback")

            if score >= 80:
                st.success(
                    "Excellent match! Your resume is highly aligned with the job description."
                )
            elif score >= 60:
                st.warning(
                    "Good match, but adding some missing skills could improve your chances."
                )
            else:
                st.error(
                    "Low match score. Consider tailoring your resume."
                )

            # AI Review
            st.subheader("🤖 AI Resume Review")

            if st.button("Generate AI Review"):

                with st.spinner(
                    "Analyzing Resume with AI..."
                ):

                    try:

                        ai_review = review_resume(
                            resume_text,
                            job_description
                        )

                        st.session_state["ai_review"] = (
                            ai_review
                        )

                    except Exception as e:

                        st.warning(
                            f"AI Review unavailable: {e}"
                        )

            if st.session_state["ai_review"]:
                st.markdown(
                    st.session_state["ai_review"]
                )

            # PDF Report
            if generate_pdf_report:

                st.subheader("📥 Full ATS PDF Report")

                if st.button(
                    "Generate PDF Report"
                ):

                    try:

                        report_file = "ATS_Report.pdf"

                        generate_pdf_report(
                            filename=report_file,
                            final_score=final_score,
                            match_score=score,
                            structure_score=structure_score,
                            strength_score=strength_score,
                            matched_keywords=matched_keywords,
                            missing_keywords=missing_keywords,
                            sections=sections,
                            ai_review=st.session_state[
                                "ai_review"
                            ]
                        )

                        with open(
                            report_file,
                            "rb"
                        ) as pdf_file:

                            st.download_button(
                                label="⬇ Download ATS Report",
                                data=pdf_file,
                                file_name="ATS_Report.pdf",
                                mime="application/pdf"
                            )

                    except Exception as e:
                        st.error(str(e))

        else:
            st.info(
                "📋 Please paste a Job Description to start ATS analysis."
            )

    except Exception as e:

        st.error(
            f"Error reading resume: {str(e)}"
        )

else:

    st.info(
        "📄 Please upload a PDF resume to begin."
    )




