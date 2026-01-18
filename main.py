import json
from core.pipeline import ResumeScreeningPipeline
from utils.file_loader import load_job_description, FileLoadError
def main():
    try:
        resume_path = input("Enter resume file path: ")
        jd_path = input("Enter job description (.txt) file path: ")

        job_description = load_job_description(jd_path)

        pipeline = ResumeScreeningPipeline()
        result = pipeline.run(resume_path, job_description)

        print("\n=== FINAL DECISION ===")
        print(json.dumps(result, indent=2))

    except FileLoadError as e:
        print("\n[ERROR]")
        print(str(e))
        print("Recommendation: Requires human review")

    except Exception as e:
        print("\n[UNEXPECTED ERROR]")
        print(str(e))

if __name__ == "__main__":
    main()
