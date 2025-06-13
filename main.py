from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class QuestionRequest(BaseModel):
    question: str

# ✅ Response model
@app.post("/api/")
async def answer_question(request: QuestionRequest):
    # Dummy logic for testing — replace this with actual logic later
    return {
        "answer": "Use `gpt-3.5-turbo-0125` for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            }
        ]
    }

