from sqlalchemy.ext.asyncio import AsyncSession

from src.app.notes import NoteModels
from src.app.notes import NoteSchemas


def create_note(data: NoteSchemas, db: AsyncSession, id: int):
    note = NoteModels(
        title=data.title,
        subtitle=data.subtitle,
        introduction=data.introduction,
        main_text=data.main_text,
        user_id=id
    )

    try:
        db.add(note)
        db.commit()
        db.refresh(note)
    except Exception as e:
        print(e)

    return note


def get_notes(id: int, db: AsyncSession):
    return db.query(NoteModels).filter(NoteModels.user_id == id).all()


def update(data: NoteSchemas, db: AsyncSession, note_id: int, user_id: int):
    note = db.query(NoteModels).filter(NoteModels.user_id == user_id, NoteModels.id == note_id).first()
    note.title = data.title
    note.subtitle = data.subtitle
    note.introduction = data.introduction
    note.main_text = data.main_text

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def remove(db: AsyncSession, note_id: int, user_id):
    note = db.query(NoteModels).filter(NoteModels.user_id == user_id, NoteModels.id == note_id).delete()

    db.commit()

    return note
