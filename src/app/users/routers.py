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
    return await user_services.create_user(data, db)


@router.get('/{id}')
async def get(user_id: int = None, db: AsyncSession = Depends(get_session)):
    return await user_services.get_user(user_id, db)


@router.put('/{id}')
async def update(user_id: int = None, data: UserSchemas = None, db: AsyncSession = Depends(get_session)):
    return await user_services.update(user_id, data, db)


@router.delete('/{id}')
async def delete(user_id: int = None, db: AsyncSession = Depends(get_session)):
    return await user_services.remove(user_id, db)
