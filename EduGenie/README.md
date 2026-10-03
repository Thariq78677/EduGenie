# EduGenie: Google Gemini Powered Learning Assistant

## 🚀 Live Demo

[Open EduGenie](https://edu-genie-8a2zbcn8z-mohamedthariq77777-9201s-projects.vercel.app/)

## Team Details

**Team Leader:** Mohamed Thariq

**Team Members:**
- Nandha Kumar
- Muniyappan
- Mohanakrishnan

---

## Project Overview

EduGenie is a Google Gemini powered learning assistant designed to help students understand academic topics, clarify doubts, revise content, practice through quizzes, and receive personalized learning recommendations.

The system uses Generative AI to provide simplified explanations and learning support through a student-friendly interface.

---

## Problem Statement

Students often face difficulty understanding complex concepts, revising long passages, and finding structured practice resources.

Traditional learning resources may not provide instant, simplified, and personalized support in one place.

EduGenie addresses this problem by providing AI-powered learning assistance through a single application.

---

## Key Features

- AI-powered Question & Answer
- Simplified topic explanations
- AI-generated quizzes
- Text summarization
- Personalized learning recommendations
- Student-friendly interface
- Fast API-based backend
- Google Gemini integration

---

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### AI
- Google Gemini API

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## System Flow

Student
↓
EduGenie Interface
↓
FastAPI Backend
↓
Google Gemini API
↓
AI Processing
↓
Learning Output
↓
Student

---

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/qa` | POST | Answer student questions |
| `/explain` | POST | Explain academic topics |
| `/quiz` | POST | Generate quizzes |
| `/summarize` | POST | Summarize educational text |
| `/learn/recommendations` | POST | Provide learning recommendations |

---

## Project Structure

```text
EduGenie/
│
├── static/
├── templates/
│
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md