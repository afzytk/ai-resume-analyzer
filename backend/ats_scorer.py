import re

REQUIRED_SECTIONS = ["experience", "education", "skills", "projects"]

KEYWORDS = ["python", "fastapi", "django", "react", "javascript", "sql", "api", "git"]


def calculate_ats_score(resume_text: str) -> dict:
    text = resume_text.lower()

    score = 0
    feedback = []

    # Section presence (40 points)
    section_score = 0
    missing_sections = []

    for section in REQUIRED_SECTIONS:
        if section in text:
            section_score += 10
        else:
            missing_sections.append(section)
            feedback.append(f"Add or improve the '{section}' section")

    score += section_score

    # Keyword matching (40 points)
    matched_keywords = []

    for keyword in KEYWORDS:
        if re.search(rf"\b{keyword}\b", text):
            matched_keywords.append(keyword)

    keyword_score = int((len(matched_keywords) / len(KEYWORDS)) * 40)
    score += keyword_score

    # Resume length (20 points)
    word_count = len(text.split())
    if word_count >= 300:
        score += 20
    else:
        feedback.append("Resume is too short; aim for at least 300 words")

    return {
        "ats_score": min(score, 100),
        "matched_keywords": matched_keywords,
        "missing_sections": missing_sections,
        "feedback": feedback,
    }
