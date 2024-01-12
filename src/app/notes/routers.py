from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database import get_session

from src.app.notes import note_service
from src.app.notes import NoteSchemas


router = APIRouter(
    tags=['notes'],
    prefix='/notes'
)


@router.post('/')
async def create(data: NoteSchemas = None, db: AsyncSession = Depends(get_session), user: int = 0):
    return note_service.create_note(data, db, user)


@router.get('/{id}')
async def get(id: int = None, db: AsyncSession = Depends(get_session)):
    return note_service.get_notes(id, db)


@router.put('/{id}')
async def update(data: NoteSchemas = None, db: AsyncSession = Depends(get_session), note_id: int = None, user_id: int = None):
    return note_service.update(data, db, note_id, user_id)


@router.delete('/{id}')
async def delete(db: AsyncSession = Depends(get_session), note_id: int = None, user_id: int = None):
    return note_service.remove(db, note_id, user_id)
