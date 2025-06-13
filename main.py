# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List
import base64

app = FastAPI()

# Define request format
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

# Define response format
class Link(BaseModel):
    url: str
    text: str

class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=AnswerResponse)
async def answer_question(request: QuestionRequest):
    question = request.question.lower()
    
    # Dummy logic – replace with actual retrieval + LLM response
    if "gpt" in question:
        answer = "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question."
        links = [
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4", "text": "Use the model that’s mentioned in the question."},
            {"url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3", "text": "Just use a tokenizer to get token count and multiply."}
        ]
    else:
        answer = "Sorry, I couldn't find an answer. Please check course videos or post on Discourse."
        links = []

    return {"answer": answer, "links": links}
