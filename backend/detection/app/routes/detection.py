import json
from fastapi import APIRouter
from pydantic import BaseModel

from models.detect import is_ai_generated

app = APIRouter()


class Payload(BaseModel):
    text: str

@app.post("/detect")
async def detect_ai(payload: Payload):
    try:
        result = {"is_ai_generated": is_ai_generated(payload.text)}
    except:
        result = {"is_ai_generated": "LLM query failed"}
    return result

