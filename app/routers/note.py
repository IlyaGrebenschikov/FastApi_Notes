from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.services import note as NoteService
from app.dto import note as NoteDTO

router = APIRouter()

@router.post('/', tags=['note'])
async def create(data: NoteDTO.Note = None, db: Session = Depends(get_db), user: int = 0):
    return NoteService.create_note(data, db, user)


@router.get('/{id}', tags=['note'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return NoteService.get_notes(id, db)


@router.put('/{id}]', tags=['note'])
async def update(data: NoteDTO.Note = None, db = Depends(get_db), note_id: int = None, user_id: int = None):
    return NoteService.update(data, db, note_id, user_id)


@router.delete('/{id}', tags=['note'])
async def delete(db: Session = Depends(get_db), note_id:int = None, user_id:int = None):
    return NoteService.remove(db, note_id, user_id)