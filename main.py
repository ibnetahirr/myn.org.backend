# uvicorn main:app --reload

#main imports
import httpx
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
import requests

app = FastAPI()

OPENAI_API_KEY = config("OPENAI_API_KEY")
REALTIME_MODEL = "gpt-4o-realtime-preview-2025-06-03"

#CORS
origins = [
    'http:localhost:5173'
]

#CORS middleware
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )


@app.get("/")
async def root():
    return {"message": OPENAI_API_KEY}

# @app.get("/session")
# async def create_ephemeral_session():
#     """
#     Mint a short-lived client token the browser can use to open a WebRTC
#     connection directly to the OpenAI Realtime API.
#     NOTE: For WebRTC you do NOT set input/output audio formats (those are for WS).
#     """
#     assert OPENAI_API_KEY, "Set OPENAI_API_KEY in your environment"
#     payload = {
#         "model": REALTIME_MODEL,
#         "voice": "verse",          # pick any voice available to your account
#         "modalities": ["text", "audio"],  # request audio responses
#         # Optional: default system prompt
#         "instructions": "You are a concise, friendly realtime voice assistant.",
#     }
#     headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient(timeout=20) as client:
#         r = await client.post("https://api.openai.com/v1/realtime/sessions",
#                               headers=headers, json=payload)
#         r.raise_for_status()
#         return r.json()

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