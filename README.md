
# Aurora Member Question-Answering API

*A FastAPI service that answers natural-language questions using Aurora’s `/messages` API.*

## Overview

This project implements the **Aurora Applied AI/ML Engineer Take-Home Assignment**, which requires building a production-ready backend service that:

- Fetches member messages from Aurora’s public `/messages` API  
- Answers natural-language questions based **only on those messages**  
- Exposes a simple `POST /ask` endpoint returning:  
  `{ "answer": "..." }`  
- Analyzes the dataset  
- Explains alternative design options  

This solution uses:

- **FastAPI**  
- **OpenRouter LLM (free model)**  
- **Strict anti-hallucination prompting**  
- **Modular architecture**

---

## Project Structure

```
aurora-qa-system/
│
├── app/
│   ├── main.py
│   ├── qa_engine.py
│   ├── api_client.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 1. Setup Instructions (FULL)

### 1.1 Create Virtual Environment (venv)

**Windows**
```
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```
python3 -m venv venv
source venv/bin/activate
```

---

### 1.2 Install Dependencies

```
pip install -r requirements.txt
```

---

### 1.3 Create `.env`

```
AURORA_MESSAGES_URL="https://november7-730026606190.europe-west1.run.app/messages"
OPENROUTER_API_KEY="your_key_here"
OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

---

### 1.4 Run the Server

```
uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

---

## 2. API Usage

### POST `/ask`

**Body**
```json
{
  "question": "......."
}
```

**Response**
```json
{
  "answer": "........."
}
```

---

## 3. How It Works

- `api_client.py` → fetches and cleans messages  
- `qa_engine.py` → LLM reasoning using anti-hallucination rules  
- Uses OpenRouter model: `qwen/qwen2.5-7b-instruct`  

---

## 4. Security Notes

- Never commit `.env`  
- Use `.env`  
- Keep API keys private  

---

## 5. Conclusion

This project fulfills all assignment requirements:

- Natural-language Q&A  
- `/ask` endpoint  
- Based on Aurora messages  
- Anti-hallucination output  
- Dataset analysis  
- Alternative methods  
- Fully reproducible using venv + requirements  

---
