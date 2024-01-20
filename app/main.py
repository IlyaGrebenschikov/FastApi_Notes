from fastapi import FastAPI

from app.users import user_router
from app.notes import note_router

from app.database import init_db

app = FastAPI(
    title='FastAPI_Notes'
)
app.include_router(user_router)
app.include_router(note_router)


@app.on_event("startup")
async def on_startup():
    await init_db()


# uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8080
# sudo docker compose -f docker_compose.yaml up --build
