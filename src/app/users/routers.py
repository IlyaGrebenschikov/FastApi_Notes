from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.database import get_session

from src.app.users import user_services
from src.app.users import UserSchemas


router = APIRouter(
    tags=['users'],
    prefix='/users'
)


@router.post('/')
async def create(data: UserSchemas = None, db: AsyncSession = Depends(get_session)):
    return user_services.create_user(data, db)


@router.get('/{id}')
async def get(id: int = None, db: AsyncSession = Depends(get_session)):
    return user_services.get_user(id, db)


@router.put('/{id}')
async def update(id: int = None, data: UserSchemas = None, db: AsyncSession = Depends(get_session)):
    return user_services.update(data, db, id)


@router.delete('/{id}')
async def delete(id: int = None, db: AsyncSession = Depends(get_session)):
    return user_services.remove(db, id)
