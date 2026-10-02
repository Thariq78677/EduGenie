# EduGenie – Google Gemini Powered Learning Assistant

## Overview
EduGenie is a lightweight AI-powered educational assistant designed to support students with academic learning. It helps users ask questions, understand difficult concepts, create quizzes, summarize content, and follow guided learning paths using Google Gemini.

## Problem Statement
Students often struggle with understanding complex topics, revising large amounts of material, and staying motivated during self-learning. They need fast, simple, and structured support without relying on traditional classroom dependency.

## Proposed Solution
EduGenie uses generative AI to provide instant academic support. The system turns difficult ideas into simple explanations, answers quick learning questions, creates quizzes for self-assessment, summarizes educational text, and recommends a structured learning path.

## Features
- AI Question Answering
- Concept Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path

## Technology Stack
- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja2
- Uvicorn
- python-dotenv

## System Architecture
User → HTML/CSS/JavaScript Frontend → FastAPI Backend → EduGenie Modules → Google Gemini API → Response → Frontend Display

## Project Structure
- [1. Brainstorming & Ideation](1.%20Brainstorming%20&%20Ideation)
- [2. Requirement Analysis](2.%20Requirement%20Analysis)
- [3. Project Design Phase](3.%20Project%20Design%20Phase)
- [4. Project Planning Phase](4.%20Project%20Planning%20Phase)
- [5. Project Development Phase](5.%20Project%20Development%20Phase)
- [6. Project Testing](6.%20Project%20Testing)
- [7. Project Documentation](7.%20Project%20Documentation)
- [8. Project Demonstration](8.%20Project%20Demonstration)

## Installation
1. Install Python 3.10 or above.
2. Create a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Create a `.env` file using the sample file:
```bash
copy .env.example .env
```
Then replace the placeholder value with your real Gemini API key.

## Running the Project
```bash
uvicorn main:app --reload
```
Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## API Endpoints
| Endpoint | Purpose |
| --- | --- |
| /qa | Question Answering |
| /explain | Concept Explanation |
| /quiz | Quiz Generation |
| /summarize | Summarization |
| /learn/recommendations | Learning Path |

## Testing
Testing is performed through the FastAPI documentation and direct API requests. Gemini API testing requires a valid `GEMINI_API_KEY`.

## Future Enhancements
- Multi-language support
- Student profile personalization
- Topic difficulty adjustments
- Better analytics and dashboards
- Offline fallback modes

## Project Documentation
- [1. Brainstorming & Ideation/Problem Statement.md](1.%20Brainstorming%20&%20Ideation/Problem%20Statement.md)
- [2. Requirement Analysis/Functional Requirements.md](2.%20Requirement%20Analysis/Functional%20Requirements.md)
- [3. Project Design Phase/Project Design.md](3.%20Project%20Design%20Phase/Project%20Design.md)
- [4. Project Planning Phase/Project Timeline.md](4.%20Project%20Planning%20Phase/Project%20Timeline.md)
- [5. Project Development Phase/Development README.md](5.%20Project%20Development%20Phase/Development%20README.md)
- [6. Project Testing/Test Plan.md](6.%20Project%20Testing/Test%20Plan.md)
- [7. Project Documentation/Project Report.md](7.%20Project%20Documentation/Project%20Report.md)
- [8. Project Demonstration/Demo Guide.md](8.%20Project%20Demonstration/Demo%20Guide.md)

## Author
Student Name:
College:
Department:
Course:
Naan Mudhalvan:
