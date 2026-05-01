from fastapi import FastAPI
from app.api.routes import logs

app = FastAPI(title="Log Intelligence Engine")

app.include_router(logs.router)


@app.get("/")
def root():
    return {"message": "API is running"}
