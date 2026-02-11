import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
from resume_analyzer_groq import analyze_resume

# Load GROQ_API_KEY
load_dotenv()

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 Resume Analyzer")

# Upload resume PDF
uploaded_pdf = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Paste Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Analyze button
if st.button("Analyze Resume"):
    if not uploaded_pdf:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please paste the job description.")
    else:
        with st.spinner("Analyzing resume..."):
            try:
                resume_text = extract_text_from_pdf(uploaded_pdf)
                result = analyze_resume(resume_text, job_description)

                st.success("Analysis Complete")

                st.subheader("Resume Analysis")
                st.text(result)

            except Exception as e:
                st.error(str(e))
