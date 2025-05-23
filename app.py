import streamlit as st
from Backend.generator import generate_all_outputs

st.set_page_config(page_title="Smart Resume Agent", layout="wide")

st.title("🧠 Smart Resume & Cover Letter Generator Agent")
st.write("Upload your resume and a job description to get tailored outputs.")

resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_file = st.file_uploader("Upload Job Description", type=["txt", "pdf", "docx"])

if st.button("Generate"):
    if resume_file and job_file:
        with st.spinner("Processing..."):
            results = generate_all_outputs(resume_file, job_file)
            st.subheader("✅ Tailored Resume Lines")
            st.write(results["resume_lines"])

            st.subheader("📝 Cover Letter")
            st.write(results["cover_letter"])

            st.subheader("❓ Interview Prep Q&A")
            st.write(results["interview_qa"])

            st.subheader("📊 Skill Gap Analysis")
            st.write(results["skill_gap"])
    else:
        st.warning("Please upload both files.")
