from fastapi import FastAPI
from app.api.routes import logs
from app.api.routes import health
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest

app = FastAPI(
    title="LogSleuth",
    description="Asynchronous log ingestion and analysis platform",
    version="1.0.0"
)
app.include_router(logs.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {
    "application": "LogSleuth",
    "status": "running",
    "version": "1.0.0"
}

@app.get("/metrics")
def metrics():

    return PlainTextResponse(
        generate_latest().decode("utf-8")
    )
