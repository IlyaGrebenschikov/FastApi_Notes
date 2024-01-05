from fastapi import FastAPI
import uvicorn
from app.database import session, engine, Base, get_db
from app.routers import user as UserRouter
from app.routers import note as NoteRouter


Base.metadata.create_all(engine)

app = FastAPI(
    title='Notes_App'
)
app.include_router(UserRouter.router, prefix='/user')
app.include_router(NoteRouter.router, prefix='/note')

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)