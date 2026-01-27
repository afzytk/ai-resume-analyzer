from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os

from resume_parser import (
    extract_text_from_pdf,
    extract_text_from_docx
)
from ats_scorer import (
    calculate_ats_score,
    analyze_resume_for_job
)

# -------------------------
# App initialization
# -------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routes
# -------------------------

@app.get("/")
def root():
    return {"status": "FastAPI backend running"}


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    job_role: str | None = Form(None),
    job_description: str | None = Form(None)
):
    filename = file.filename.lower()
    file_bytes = await file.read()

    # Extract resume text
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_bytes)

    elif filename.endswith(".docx"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        text = extract_text_from_docx(tmp_path)
        os.remove(tmp_path)

    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported"
        )

    # General ATS score
    ats_result = calculate_ats_score(text)

    # Job-specific analysis
    job_result = analyze_resume_for_job(
        resume_text=text,
        job_description=job_description,
        job_role=job_role
    )

    return {
        "filename": file.filename,
        "ats_score": ats_result["ats_score"],
        "job_fit_score": job_result["job_fit_score"],
        "matched_skills": job_result["matched_skills"],
        "missing_skills": job_result["missing_skills"],
        "missing_sections": ats_result["missing_sections"],
        "feedback": ats_result["feedback"],
        "suggestions": job_result["suggestions"]
    }
