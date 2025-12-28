from fastapi import FastAPI
from app.api.api_router import api_router

app = FastAPI(
    title="FastAPI + Poetry",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
