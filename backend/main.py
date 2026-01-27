from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os

from resume_parser import (
    extract_text_from_pdf,
    extract_text_from_docx
)
from ats_scorer import calculate_ats_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "FastAPI backend running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    filename = file.filename.lower()
    file_bytes = await file.read()

    # Extract text from resume
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

    # ATS scoring
    ats_result = calculate_ats_score(text)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "ats_score": ats_result["ats_score"],
        "matched_keywords": ats_result["matched_keywords"],
        "missing_sections": ats_result["missing_sections"],
        "feedback": ats_result["feedback"]
    }
