import re

# -------------------------
# Resume quality config
# -------------------------

REQUIRED_SECTIONS = [
    "experience",
    "education",
    "skills",
    "projects"
]

BASE_KEYWORDS = [
    "python",
    "fastapi",
    "django",
    "react",
    "javascript",
    "sql",
    "api",
    "git"
]

# -------------------------
# Skill knowledge base
# -------------------------

ROLE_SKILLS = {
    "frontend_developer": {
        "html", "css", "javascript", "react", "rest"
    },
    "backend_developer": {
        "python", "fastapi", "django", "sql", "rest", "api"
    },
    "fullstack_developer": {
        "html", "css", "javascript", "react",
        "python", "fastapi", "sql", "rest"
    },
    "data_analyst": {
        "python", "sql", "excel", "pandas"
    },
    "data_scientist": {
        "python", "pandas", "numpy", "machine", "learning"
    },
    "devops_engineer": {
        "docker", "aws", "linux", "ci", "cd"
    }
}

KNOWN_SKILLS = set().union(*ROLE_SKILLS.values())

STOPWORDS = {
    "developer", "engineer", "software", "frontend", "backend",
    "role", "looking", "experience", "responsible",
    "team", "years", "with", "and", "for", "the", "to",
    "of", "in", "on", "a", "an", "is", "are"
}


# -------------------------
# Utility functions
# -------------------------

def extract_words(text: str):
    if not text:
        return set()
    return set(re.findall(r"\b[a-zA-Z]+\b", text.lower()))


def extract_skills_from_text(text: str):
    words = extract_words(text)
    return {w for w in words if w in KNOWN_SKILLS}


# -------------------------
# ATS score (job-agnostic)
# -------------------------

def calculate_ats_score(resume_text: str) -> dict:
    text = resume_text.lower()
    score = 0
    feedback = []
    missing_sections = []

    # Section presence (40)
    for section in REQUIRED_SECTIONS:
        if section in text:
            score += 10
        else:
            missing_sections.append(section)
            feedback.append(f"Add or improve the '{section}' section")

    # Keyword presence (40)
    matched_keywords = [
        kw for kw in BASE_KEYWORDS
        if re.search(rf"\b{kw}\b", text)
    ]
    score += int((len(matched_keywords) / len(BASE_KEYWORDS)) * 40)

    # Length (20)
    if len(text.split()) >= 300:
        score += 20
    else:
        feedback.append("Resume is too short; aim for at least 300 words")

    return {
        "ats_score": min(score, 100),
        "matched_keywords": matched_keywords,
        "missing_sections": missing_sections,
        "feedback": feedback
    }


# -------------------------
# Job-specific analysis
# -------------------------

def analyze_resume_for_job(
    resume_text: str,
    job_description: str | None,
    job_role: str | None
) -> dict:

    resume_skills = extract_skills_from_text(resume_text)

    jd_skills = extract_skills_from_text(job_description or "")

    # Role-based fallback
    if not jd_skills and job_role in ROLE_SKILLS:
        jd_skills = ROLE_SKILLS[job_role]

    if not jd_skills:
        return {
            "job_fit_score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "suggestions": [
                "Provide a detailed job description or select a job role."
            ]
        }

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)

    job_fit_score = int((len(matched) / len(jd_skills)) * 100)

    suggestions = []

    # Improved feedback (where to fix)
    if missing:
        suggestions.append(
            "Add the missing skills to your Skills section: "
            + ", ".join(missing)
        )
        suggestions.append(
            "Mention these skills in Projects or Experience with measurable impact."
        )

    if job_fit_score < 60:
        suggestions.append(
            "Resume is weakly aligned. Tailor project descriptions to this role."
        )
    elif job_fit_score < 80:
        suggestions.append(
            "Resume is moderately aligned. Strengthen impact metrics."
        )
    else:
        suggestions.append(
            "Resume is well aligned with this role."
        )

    return {
        "job_fit_score": job_fit_score,
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions
    }
