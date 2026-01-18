class JobMatcherAgent:
    def run(self, skills_data: dict, job_description: str) -> dict:
        jd_text = job_description.lower()
        matched = [s for s in skills_data["skills"] if s in jd_text]

        if skills_data["skill_count"] == 0:
            match_score = 0.0
        else:
            match_score = len(matched) / skills_data["skill_count"]

        return {
            "matched_skills": matched,
            "match_score": round(match_score, 2),
            "low_signal": skills_data["low_signal"]
        }
