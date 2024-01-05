from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.services import user as UserService
from app.dto import user as UserDTO


router = APIRouter()

@router.post('/', tags=['user'])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/{id}', tags=['user'])
async def update(id: int = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)

@router.delete('/{id}', tags=['user'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)