from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from routes import ping, detection, feedback

app = FastAPI()

# Add Prometheus metrics to the app
Instrumentator().instrument(app).expose(app)

app.include_router(detection.app)
app.include_router(feedback.app)
app.include_router(ping.app)
