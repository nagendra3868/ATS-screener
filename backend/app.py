from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import pdfplumber
from docx import Document

from ats_engine import analyze_resume

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Read Resume
# -----------------------------

def extract_resume_text(path):

    extension = os.path.splitext(path)[1].lower()

    if extension == ".txt":

        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".pdf":

        text = ""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    elif extension == ".docx":

        doc = Document(path)

        return "\n".join(
            paragraph.text for paragraph in doc.paragraphs
        )

    else:
        return None


# -----------------------------
# Home
# -----------------------------

@app.route("/")
def home():

    return jsonify({
        "message": "Smart ATS Backend Running"
    })


# -----------------------------
# Analyze Resume
# -----------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:

        return jsonify({
            "error": "Resume not uploaded"
        }), 400

    role = request.form.get("role")

    if not role:

        return jsonify({
            "error": "Please select a role"
        }), 400

    resume = request.files["resume"]

    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    resume.save(file_path)

    resume_text = extract_resume_text(file_path)
    print("\n" + "=" * 60)
    print("RESUME TEXT")
    print("=" * 60)
    print(resume_text)
    print("=" * 60 + "\n")
    if not resume_text:

        return jsonify({
            "error": "Unsupported file format"
        }), 400

    result = analyze_resume(
        resume_text,
        role
    )

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )
