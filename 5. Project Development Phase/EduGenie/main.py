import logging
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Student question")


class TopicRequest(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to explain or recommend")


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Educational text for summarization or quiz generation")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/qa")
async def ask_question(payload: QuestionRequest):
    try:
        result = answer_question(payload.question)
        return {"answer": result}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logging.exception("Error in /qa")
        raise HTTPException(status_code=500, detail="Unable to answer the question right now. Please try again later.") from exc


@app.post("/explain")
async def explain(payload: TopicRequest):
    try:
        result = explain_topic(payload.topic)
        return {"explanation": result}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logging.exception("Error in /explain")
        raise HTTPException(status_code=500, detail="Unable to explain this topic right now. Please try again later.") from exc


@app.post("/quiz")
async def quiz(payload: TextRequest):
    try:
        result = generate_quiz(payload.text)
        return {"quiz": result}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logging.exception("Error in /quiz")
        raise HTTPException(status_code=500, detail="Unable to generate the quiz right now. Please try again later.") from exc


@app.post("/summarize")
async def summarize(payload: TextRequest):
    try:
        result = summarize_text(payload.text)
        return {"summary": result}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logging.exception("Error in /summarize")
        raise HTTPException(status_code=500, detail="Unable to summarize the text right now. Please try again later.") from exc


@app.post("/learn/recommendations")
async def learn_recommendations(payload: TopicRequest):
    try:
        result = get_learning_recommendations(payload.topic)
        return {"recommendations": result}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        logging.exception("Error in /learn/recommendations")
        raise HTTPException(status_code=500, detail="Unable to generate learning recommendations right now. Please try again later.") from exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
