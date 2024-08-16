from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/info")
async def info():
    return {
        "app name":settings.app_name
    }