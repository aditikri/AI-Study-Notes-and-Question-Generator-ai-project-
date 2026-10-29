# AI Study Notes and Question Generator 📚

## About the Project
AI Study Notes and Question Generator is a Python-based web application that helps students create study notes and practice questions using Google's Gemini AI. It provides an easy way to revise academic topics and prepare for exams.

## Features
- Generate concise study notes.
- Create 5 MCQs with options and correct answers.
- Generate 5 short-answer questions with answers.
- Accept a topic or pasted academic text.
- Download generated study material as a TXT file.
- Simple and user-friendly interface.

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Project Structure
```text
AI-Study-Generator/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

**1. Clone or download the project** and open the folder in VS Code.

**2. Create and activate a virtual environment** from the parent project directory:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the required packages:**

```bash
pip install streamlit google-genai python-dotenv
```

**4. Configure the API key.**

Create a `.env` file inside `AI-Study-Generator` and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own API key. Do not share or upload your real key.

**5. Run the application** from the parent directory:

```bash
python -m streamlit run AI-Study-Generator/app.py
```

Open the local URL displayed in the terminal.

## How to Use
1. Enter a topic or paste academic text.
2. Select **Study Notes** or **Practice Questions**.
3. Click **Generate**.
4. Review the generated content.
5. Download the study material as a TXT file.

## Learning Outcomes
- Learned Python-based web application development.
- Integrated a generative AI API into an application.
- Used environment variables to protect API credentials.
- Explored AI-assisted learning and question generation.
- Practiced error handling and dependency management.

## Limitations
- Requires an internet connection.
- Generation depends on API availability and usage limits.
- AI-generated content may contain errors, so users should verify important information.

## Future Enhancements
- PDF and DOCX file uploads.
- Interactive quizzes with scores.
- Multiple-language support.
- Question difficulty selection.
- Saving and reviewing previous study materials.

## Security
Add `.env` and `.venv/` to `.gitignore`. Never upload your API key to a public repository.

## Author
MCA Student

## Purpose
Developed as an academic mini-project to demonstrate Python programming and generative AI integration.