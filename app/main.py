from fastapi import FastAPI
from app.api.routes import logs
from app.api.routes import health
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
