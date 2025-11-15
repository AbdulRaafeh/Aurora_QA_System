from pydantic import BaseModel
from fastapi import FastAPI
from app.qa_engine import answer_question

app = FastAPI(title="Aurora Question Answering API")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: Question):
    answer = answer_question(payload.question)
    return {"answer": answer}
# @app.post("/ask")
# def ask_question():
#     answer = answer_question("When is Layla planning her trip to London?")
#     return {"answer": answer}
