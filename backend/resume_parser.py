import pdfplumber
import docx2txt
import tempfile


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    with pdfplumber.open(tmp_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_text_from_docx(file_path: str) -> str:
    return docx2txt.process(file_path).strip()
