from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an ATS-style resume analyzer used for resume screening."
    ),
    (
        "human",
        """
Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume against the job description and provide the result in clear, plain text using ONLY the sections below.

Role Suitability:
- ATS Match Score (out of 100)
- Brief explanation of why this score was given

Technical Skills Matching the Job Description:
- List only the skills that appear in BOTH the resume and the job description

Soft Skills Matching the Job Description:
- List only the matching soft skills

Experience Matching the Job Description:
- Summarize relevant experience and years, if mentioned

Suggestions for Improvement:
- Actionable suggestions to improve ATS match and job relevance

Rules:
- Do NOT use JSON
- Do NOT use code blocks or markdown formatting
- Use simple bullet points
- Do NOT add extra sections or headings
"""
    )
])

parser = StrOutputParser()
chain = prompt | llm | parser

def analyze_resume(resume_text: str, job_description: str) -> str:
    return chain.invoke({
        "resume_text": resume_text,
        "job_description": job_description
    })
