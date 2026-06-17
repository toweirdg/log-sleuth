from fastapi import FastAPI
from app.api.routes import logs

app = FastAPI(
    title="LogSleuth",
    description="Asynchronous log ingestion and analysis platform",
    version="1.0.0"
)
app.include_router(logs.router)


@app.get("/")
def root():
    return {
    "application": "LogSleuth",
    "status": "running",
    "version": "1.0.0"
}
