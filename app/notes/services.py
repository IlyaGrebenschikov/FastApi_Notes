from typing import Optional, Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.notes import NoteModels
from app.notes import NoteSchemas

from sqlalchemy import select, delete

from fastapi import HTTPException

from app.users import get_user


async def create_note(user_id: int, data: NoteSchemas, db: AsyncSession) -> Optional[NoteModels | dict]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    note = NoteModels(**data.model_dump())
    note.user_id = user_id
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


async def get_notes(user_id: int, limit: int, db: AsyncSession) -> Optional[NoteModels | Any]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    stmt = (
        select(NoteModels).
        filter(NoteModels.user_id == user_id).
        limit(limit)
    )
    result = await db.execute(stmt)
    note = result.scalars().all()
    return note


async def get_note(user_id: int, note_id: int, db: AsyncSession) -> Optional[NoteModels]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    stmt = (
        select(NoteModels).
        filter(NoteModels.user_id == user_id, NoteModels.id == note_id)
    )
    result = await db.execute(stmt)
    note = result.scalar()
    return note


async def update(user_id: int, note_id: int, data: NoteSchemas, db: AsyncSession) -> Optional[NoteModels | Any]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    try:
        stmt = (
            select(NoteModels).
            filter(NoteModels.user_id == user_id, NoteModels.id == note_id)
        )
        result = await db.execute(stmt)
        note = result.scalars().one()
        note.title = data.title
        note.subtitle = data.subtitle
        note.main_text = data.main_text
        await db.commit()
        await db.refresh(note)
    except Exception:
        raise HTTPException(404, 'Note not found')
    return note


async def remove(user_id: int, note_id: int, db: AsyncSession) -> Optional[NoteModels | Any]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    try:
        stmt = (
            delete(NoteModels).
            filter(NoteModels.user_id == user_id, NoteModels.id == note_id)
        )
        await db.execute(stmt)
        await db.commit()
    except Exception:
        raise HTTPException(404, 'Note not found')
    return {
        'result': 'deleted'
    }
