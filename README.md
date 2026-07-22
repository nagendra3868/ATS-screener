# 🚀 Smart ATS Resume Keyword Screener

A modern AI-inspired **Applicant Tracking System (ATS)** that analyzes resumes based on job-specific keywords and provides an ATS compatibility score. This project helps job seekers understand how well their resumes match different job roles.

---

## 📌 Features

- 📄 Upload Resume (PDF, DOCX, TXT)
- 🎯 Role-Based Resume Analysis
- 📊 ATS Compatibility Score
- ✅ Matched Keywords
- ❌ Missing Keywords
- 🌙 Light & Dark Mode
- 📱 Responsive User Interface
- ⚡ Fast Resume Processing
- 🎨 Modern Dashboard Design

---

## 🖥️ Screenshots

> Add screenshots of your project here.

### Home Page

![Home](images/home.png)

### Dashboard

![Dashboard](images/dashboard.png)

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Libraries
- pdfplumber
- python-docx

---

## 📂 Project Structure

```text
ATS-Screener/
│
├── backend/
│   ├── app.py
│   ├── ats_engine.py
│   ├── requirements.txt
│   ├── uploads/
│   └── keywords/
│       ├── Python Developer.csv
│       ├── Data Analyst.csv
│       ├── Java Developer.csv
│       ├── Full Stack Developer.csv
│       └── Automation Developer.csv
│
├── images/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

---

## 📊 Supported Job Roles

- Python Developer
- Data Analyst
- Java Developer
- Full Stack Developer
- Automation Developer

Each role has its own keyword database stored as a CSV file.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/nagendra3868/ATS-Screener.git
```

Move into the project folder

```bash
cd ATS-Screener
```

Install dependencies

```bash
pip install -r backend/requirements.txt
```

Run the Flask server

```bash
cd backend
python app.py
```

Open `index.html` using Live Server or any local web server.

---

## 📈 How It Works

1. Upload your resume.
2. Select the desired job role.
3. The backend extracts text from the resume.
4. Keywords are loaded from the selected role's CSV file.
5. Resume keywords are compared against required skills.
6. ATS Score is calculated.
7. The dashboard displays:
   - ATS Score
   - Matched Skills
   - Missing Skills
   - Overall Rating

---

## 📊 ATS Score Formula

```text
ATS Score =
(Number of Matched Keywords / Total Keywords) × 100
```

---

## 🌙 Dark Mode

The application includes a fully functional Light and Dark mode for improved user experience.

---

## 📌 Future Enhancements

- 🤖 AI Resume Suggestions
- 📄 Resume Summary Generation
- 🎯 Skill Gap Analysis
- 📈 Resume Ranking
- 📧 Email Report Generation
- 📊 Interactive Analytics Dashboard
- ☁️ Cloud Deployment
- 🧠 Semantic Skill Matching
- 🔍 Multi-role Resume Comparison

---

## 👨‍💻 Author

**Nagendra**

GitHub:
https://github.com/nagendra3868

---

## 📄 License

This project is developed for learning, portfolio, and hackathon purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
