from fastapi import FastAPI

import uvicorn

from src.app.users import user_router
from src.app.notes import note_router


app = FastAPI(
    title='FastAPI_Notes'
)
app.include_router(user_router)
app.include_router(note_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
