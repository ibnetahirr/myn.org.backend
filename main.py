# uvicorn main:app --reload

#main imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import requests
import os

app = FastAPI()

# OPENAI_API_KEY = config("OPENAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REALTIME_MODEL = "gpt-4o-realtime-preview-2025-06-03"

#CORS
origins = [
    'https://myn-org.vercel.app/'
]

#CORS middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )


@app.get("/session")
async def get_session():
    r = requests.post(
        "https://api.openai.com/v1/realtime/sessions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-realtime-preview-2024-12-17",
            "voice": "verse",
        },
    )
    return r.json()