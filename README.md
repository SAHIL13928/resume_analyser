# resume_analyser
#  Agentic Resume Screening & Shortlisting Assistant

This project implements an **agentic, explainable resume screening system** that evaluates how well a candidate’s resume matches a given job description and recommends next steps in the hiring process.

The system is designed as a **multi-agent pipeline**, where each agent has a clear responsibility and passes structured data to the next agent, similar to how a real hiring committee works.

This project focuses on **clarity of reasoning, explainability, robustness, and documentation quality**, rather than UI or deployment.

---

##  What This System Does

### Inputs
- A resume file (`.pdf` or `.docx`)
- A job description file (`.txt`)

### Output
A structured JSON decision containing:

```json
{
  "match_score": 0.0,
  "recommendation": "Proceed to interview | Needs manual review | Reject",
  "requires_human": true,
  "confidence": 0.0,
  "reasoning_summary": "Human-readable explanation"
}
```

---

##  Architecture Overview

The system is intentionally **agentic**, not a single linear script.

### Agent Pipeline

```
Resume File
   ↓
ResumeParserAgent
   ↓
SkillExtractionAgent
   ↓
JobMatcherAgent
   ↓
DecisionAgent
   ↓
Final JSON Decision
```

Each agent:
- Has a **single responsibility**
- Produces **structured output**
- Passes state forward
- Enables explainable decision-making

---

##  Agent Responsibilities

### 1. ResumeParserAgent
- Reads `.pdf` or `.docx` resumes
- Extracts raw text
- Handles empty or unreadable resumes gracefully

### 2. SkillExtractionAgent
- Extracts predefined technical skills from resume text
- Flags **low-signal resumes** when insufficient skills are found

### 3. JobMatcherAgent
- Compares extracted skills against the job description
- Computes a normalized match score
- Preserves uncertainty signals

### 4. DecisionAgent
- Applies decision thresholds
- Handles low-confidence and edge cases
- Routes uncertain cases to **human review**
- Produces explainable reasoning

---

##  Why This Is “Agentic”

This system avoids common anti-patterns such as:
- One large function doing everything
- A single massive prompt or black-box decision
- Simple keyword filtering with no reasoning

Instead, it demonstrates:
- Multiple agents with clear responsibilities
- Structured data passing between agents
- Decision points based on intermediate outputs
- Explicit uncertainty handling
- Human-in-the-loop design

---

## ⚙️ Setup Instructions (Step-by-Step)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd resume_analyser
```

---

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**PowerShell**
```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` in your terminal.

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Prepare input files

- Resume: `.pdf` or `.docx`
- Job description: `.txt`

Example files are available in the `samples/` folder.

---

### 5. Run the system

```bash
python main.py
```

You will be prompted to enter:
```
Enter resume file path:
Enter job description (.txt) file path:
```

---

##  Example Run

### Input
```
Resume: samples/sample_resume.pdf
Job Description: samples/sample_jd.txt
```

### Output
```json
{
  "match_score": 0.75,
  "recommendation": "Proceed to interview",
  "requires_human": false,
  "confidence": 0.95,
  "reasoning_summary": "Matched skills: ['python', 'sql', 'rest']"
}
```

---

##  Error Handling & Edge Cases

The system is designed to **fail safely and transparently**.

Handled cases include:
- Invalid or missing files
- Empty resumes or job descriptions
- Scanned PDFs with no extractable text
- Low-signal resumes with insufficient information

### Design Principle
> When confidence is low, the system defers to human judgment instead of making a strong automated decision.

---

## Trade-offs & Assumptions

### Decisions Made
- Used deterministic logic instead of LLMs for reliability and explainability
- Focused on backend clarity rather than UI or deployment
- Explicitly modeled uncertainty rather than forcing binary decisions

### What Was Skipped
- Semantic skill matching (e.g., related technologies)
- Deep experience parsing (years, seniority)
- Deployment and scalability concerns

---

##  Use of AI Tools

This version **does not rely on LLMs**.

This was a deliberate choice to:
- Avoid hallucinations
- Ensure deterministic behavior

The architecture is designed so that:
- Skill extraction or job matching agents can later be replaced with LLM-based agents
- LangGraph or similar orchestration frameworks can be added with minimal refactoring

---

##  Future Improvements

If more time were available, potential improvements include:
- LLM-based semantic skill extraction
- LangGraph-based agent orchestration
- Resume section parsing (experience vs skills)
- Logging and observability
- Confidence calibration using historical data

---

##  Final Notes

This system reflects how real-world hiring automation should work:
- Transparent
- Robust to messy inputs
- Designed for collaboration between AI and humans
