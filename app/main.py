from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.users import user_router
from app.notes import note_router

from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title='FastAPI_Notes',
    lifespan=lifespan,
)
app.include_router(user_router)
app.include_router(note_router)


@app.get('/')
async def hello() -> dict:
    return {
        'hello': 'world'
    }


# uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8080
# sudo docker compose -f docker_compose.yaml up --build
