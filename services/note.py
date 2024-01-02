from models.note import Note
from sqlalchemy.orm import Session
from dto import note


def create_note(data: note.Note, db: Session, id: int):
    note = Note(
        title=data.title,
        subtitle=data.subtitle,
        introduction=data.introduction,
        main_text=data.main_text,
        user_id = id
    )
    
    try:
        db.add(note)
        db.commit()
        db.refresh(note)
    except Exception as e:
        print(e)
        
    return note


def get_notes(id: int, db: Session):
    return db.query(Note).filter(Note.user_id == id).all()


def update(data: note.Note, db: Session, note_id: int, user_id: int):
    note = db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).first()
    note.title = data.title
    note.subtitle = data.subtitle
    note.introduction = data.introduction
    note.main_text = data.main_text
    
    db.add(note)
    db.commit()
    db.refresh(note)
    
    return note


def remove(db: Session, note_id: int, user_id):
    note = db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).delete()
    
    db.commit()
    
    return note


