import os
from fastapi import APIRouter
from pydantic import BaseModel
import logging

app = APIRouter()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    filename=os.path.join(os.getenv("FEEDBACK_LOG_DIR"), "feedback.log")
)

# Create a logger
logger = logging.getLogger(__name__)

class Feedback(BaseModel):
    text: str
    prediction: float
    is_correct: bool

@app.post("/feedback")
async def save_feedback(payload: Feedback):
    logger.info(f"{payload.text}, {payload.is_correct}, {payload.prediction}")


