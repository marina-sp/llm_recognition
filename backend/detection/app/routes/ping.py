from fastapi import APIRouter

app = APIRouter()

@app.get("/ping")
async def pong():
    # provide a simple test reponse
    return {"ping": "pong!"}