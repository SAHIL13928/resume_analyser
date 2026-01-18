import pdfplumber
from docx import Document

class FileLoadError(Exception):
    pass


def load_resume(file_path: str) -> str:
    try:
        if file_path.endswith(".pdf"):
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            if not text.strip():
                raise FileLoadError("Resume PDF has no extractable text")
            return text

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            text = "\n".join(p.text for p in doc.paragraphs)
            if not text.strip():
                raise FileLoadError("Resume DOCX is empty")
            return text

        else:
            raise FileLoadError("Unsupported resume format")

    except Exception as e:
        raise FileLoadError(str(e))


def load_job_description(file_path: str) -> str:
    if not file_path.endswith(".txt"):
        raise FileLoadError("Job description must be a .txt file")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        raise FileLoadError("Job description file is empty")

    return text
