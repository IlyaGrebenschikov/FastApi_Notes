from typing import Optional, Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.notes import NoteModels
from src.app.notes import NoteSchemas

from sqlalchemy import select, delete


async def create_note(user_id: int, data: NoteSchemas, db: AsyncSession) -> Optional[NoteModels | dict]:
    note = NoteModels(**data.model_dump())
    note.user_id = user_id

    try:
        db.add(note)
        await db.commit()
        await db.refresh(note)
    except Exception as e:
        print(e)
        return {
            'result': 'status 500',
        }

    return note


async def get_notes(user_id: int, limit: int, db: AsyncSession) -> Optional[NoteModels | Any]:
    stmt = (
        select(NoteModels).
        filter(NoteModels.user_id == user_id).
        limit(limit)
    )
    result = await db.execute(stmt)
    note = result.scalars().all()

    return note


async def get_note(user_id: int, note_id: int, db: AsyncSession) -> Optional[NoteModels]:
    stmt = (
        select(NoteModels).
        filter(NoteModels.user_id == user_id, NoteModels.id == note_id)
    )
    result = await db.execute(stmt)
    note = result.scalar()

    return note


async def update(user_id: int, note_id: int, data: NoteSchemas, db: AsyncSession) -> Optional[NoteModels | Any]:
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

    return note


async def remove(user_id: int, note_id: int, db: AsyncSession) -> Optional[NoteModels | Any]:
    stmt = (
        delete(NoteModels).
        filter(NoteModels.user_id == user_id, NoteModels.id == note_id)
    )

    await db.execute(stmt)
    await db.commit()
    
    return {
        'result': 'deleted'
    }
