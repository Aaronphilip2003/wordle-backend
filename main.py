from fastapi import FastAPI # pyright: ignore[reportMissingImports]
import asyncpg
import os
from utils.rds import get_random_word
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://user:password@postgres:5432/wordle_db"

@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.create_pool(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/get-word")
async def get_word():
    try:
        word = await get_random_word(app.state.db)
        return {"word": word}
    except Exception as e:
        return {"error": str(e)}
