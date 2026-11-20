import streamlit as st
from utils import (
    extract_resume_text,
    clean_text,
    compute_similarity_score,
    get_keyword_analysis,
)

st.set_page_config(page_title="Resume vs JD Matcher", page_icon="📄", layout="centered")

st.title("📄 Resume vs Job Description Matcher")
st.write(
    "Upload your resume and paste a job description below. "
    "This tool calculates how closely your resume matches the JD "
    "using TF-IDF + Cosine Similarity, and shows which important "
    "keywords are missing from your resume."
)

st.divider()

# --- Inputs ---
resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text_input = st.text_area("Paste the Job Description here", height=250)

# --- Action ---
if st.button("🔍 Calculate Match Score", type="primary"):

    if not resume_file:
        st.warning("Please upload a resume file.")
    elif not jd_text_input.strip():
        st.warning("Please paste a job description.")
    else:
        with st.spinner("Analyzing..."):
            try:
                raw_resume_text = extract_resume_text(resume_file)
            except ValueError as e:
                st.error(str(e))
                st.stop()

            resume_clean = clean_text(raw_resume_text)
            jd_clean = clean_text(jd_text_input)

            if not resume_clean or not jd_clean:
                st.error("Couldn't extract readable text. Try a different file.")
                st.stop()

            score = compute_similarity_score(resume_clean, jd_clean)
            matched, missing = get_keyword_analysis(resume_clean, jd_clean)

        # --- Results ---
        st.divider()
        st.subheader("Match Score")

        if score >= 75:
            st.success(f"✅ {score}% Match — Strong fit!")
        elif score >= 50:
            st.warning(f"⚠️ {score}% Match — Decent, but can be improved.")
        else:
            st.error(f"❌ {score}% Match — Low similarity, resume needs tailoring.")

        st.progress(min(int(score), 100))

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matched Keywords")
            if matched:
                st.write(", ".join(matched))
            else:
                st.write("No strong keyword matches found.")

        with col2:
            st.markdown("### ❌ Missing Keywords")
            if missing:
                st.write(", ".join(missing))
                st.caption("Consider adding these (if genuinely relevant to your experience).")
            else:
                st.write("Great! No major keywords missing.")

st.divider()
st.caption("Built with Streamlit • TF-IDF • Scikit-learn")
