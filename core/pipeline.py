from agents.resume_parser import ResumeParserAgent
from agents.skill_extractor import SkillExtractionAgent
from agents.job_matcher import JobMatcherAgent
from agents.decision_maker import DecisionAgent

class ResumeScreeningPipeline:
    def __init__(self):
        self.parser = ResumeParserAgent()
        self.extractor = SkillExtractionAgent()
        self.matcher = JobMatcherAgent()
        self.decision = DecisionAgent()

    def run(self, resume_path: str, job_description: str) -> dict:
        resume_data = self.parser.run(resume_path)
        skills_data = self.extractor.run(resume_data)
        match_data = self.matcher.run(skills_data, job_description)
        final_decision = self.decision.run(match_data)

        return final_decision
