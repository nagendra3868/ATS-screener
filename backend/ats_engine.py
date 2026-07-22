import csv
import os
import re

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYWORDS_DIR = os.path.join(BASE_DIR, "keywords")


def load_keywords(role):
    """
    Load keywords from the selected role CSV.
    """

    filename = f"{role}.csv"
    filepath = os.path.join(KEYWORDS_DIR, filename)

    if not os.path.exists(filepath):
        print(f"[ERROR] Keyword file not found: {filepath}")
        return []

    keywords = []

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            keyword = row.get("keyword", "").strip().lower()

            if keyword:
                keywords.append(keyword)

    return keywords


def clean_text(text):
    """
    Clean resume text.
    """

    text = text.lower()

    # Keep letters, numbers and spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def analyze_resume(resume_text, role):
    """
    Analyze resume for the selected job role.
    """

    resume_text = clean_text(resume_text)

    target_keywords = load_keywords(role)

    if not target_keywords:
        return {
            "score": 0,
            "rating": "No Keywords Found",
            "matched_keywords": [],
            "missing_keywords": []
        }

    matched = []
    missing = []

    for keyword in target_keywords:

        # Clean keyword as well
        keyword = clean_text(keyword)

        if keyword in resume_text:
            matched.append(keyword)
        else:
            missing.append(keyword)

    score = round((len(matched) / len(target_keywords)) * 100, 2)

    if score >= 80:
        rating = "Strong Match 🟢"
    elif score >= 50:
        rating = "Partial Match 🟡"
    else:
        rating = "Needs Review 🔴"

    return {
        "score": score,
        "rating": rating,
        "matched_keywords": matched,
        "missing_keywords": missing
    }
