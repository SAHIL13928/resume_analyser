from utils.file_loader import load_resume

class ResumeParserAgent:
    def run(self, resume_path: str) -> dict:
        text = load_resume(resume_path)
        return {
            "raw_text": text,
            "length": len(text)
        }
