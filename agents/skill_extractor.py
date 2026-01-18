class SkillExtractionAgent:
    COMMON_SKILLS = [
        "python", "java", "sql", "django", "flask",
        "rest", "api", "docker", "aws", "backend"
    ]

    def run(self, resume_data: dict) -> dict:
        text = resume_data["raw_text"].lower()
        found_skills = [s for s in self.COMMON_SKILLS if s in text]

        return {
            "skills": found_skills,
            "skill_count": len(found_skills),
            "low_signal": len(found_skills) < 2
        }
