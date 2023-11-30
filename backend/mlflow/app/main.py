import os
from fastapi import FastAPI
from pydantic import BaseModel
from models.model import LLM

cache_path = os.getenv("HUGGINGFACE_MODEL_CACHE")

# Load model
model = LLM(cache_path)

# register api
app = FastAPI()


class Payload(BaseModel):
    prompt: str
    temperature: float
    max_tokens: int

@app.get("/generate")
def generate_response(payload: Payload):
    """
    A simple function that receive a review content and predict the sentiment of the content.
    :param payload:
    :return: LLM response
    """
    result = model.predict(model_input={
        "prompt": payload.prompt,
        "temperature": payload.temperature,
        "max_tokens": payload.max_tokens
    })

    return result

