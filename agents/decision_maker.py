class DecisionAgent:
    def run(self, match_data: dict) -> dict:
        score = match_data["match_score"]
        low_signal = match_data["low_signal"]

        if low_signal:
            return {
                "match_score": score,
                "recommendation": "Needs manual review",
                "requires_human": True,
                "confidence": 0.4,
                "reasoning_summary": "Insufficient signal in resume to make confident decision"
            }

        if score >= 0.7:
            recommendation = "Proceed to interview"
            requires_human = False
        elif score >= 0.4:
            recommendation = "Needs manual review"
            requires_human = True
        else:
            recommendation = "Reject"
            requires_human = False

        confidence = min(1.0, round(score + 0.2, 2))

        return {
            "match_score": score,
            "recommendation": recommendation,
            "requires_human": requires_human,
            "confidence": confidence,
            "reasoning_summary": f"Matched skills: {match_data['matched_skills']}"
        }
