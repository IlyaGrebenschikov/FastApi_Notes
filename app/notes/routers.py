from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from app.database import get_session
from app.notes import NoteSchemas
from app.notes import note_service

router = APIRouter(
    tags=['notes'],
    prefix='/notes'
)


@router.post('/')
async def create(user_id: int, data: NoteSchemas = None, db: AsyncSession = Depends(get_session)):
    return await note_service.create_note(user_id, data, db)


@router.get('/many{id}')
@cache(expire=30)
async def get_notes(user_id: int = None, limit: int = 20, db: AsyncSession = Depends(get_session)):
    return await note_service.get_notes(user_id, limit, db)


@router.get('/one{id}')
@cache(expire=30)
async def get_note(user_id: int = None, note_id: int = None, db: AsyncSession = Depends(get_session)):
    return await note_service.get_note(user_id, note_id, db)


@router.put('/{id}')
async def update(user_id: int = None, note_id: int = None, data: NoteSchemas = None,
                 db: AsyncSession = Depends(get_session)):
    return await note_service.update(user_id, note_id, data, db)


@router.delete('/{id}')
async def delete(user_id: int = None, note_id: int = None, db: AsyncSession = Depends(get_session)):
    return await note_service.remove(user_id, note_id, db)
