from fastapi import FastAPI
import uvicorn
from database import session, engine, Base, get_db
from routers import user as UserRouter

Base.metadata.create_all(engine)

app = FastAPI(
    title='Notes_App'
)
app.include_router(UserRouter.router, prefix='/user')

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=3)