from src.app.users import UserModels
from src.app.users import UserSchemas

from sqlalchemy.ext.asyncio import AsyncSession


def create_user(data: UserSchemas, db: AsyncSession):
    user = UserModels(name=data.name)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user


def get_user(id: int, db: AsyncSession):
    return db.query(UserModels).filter(UserModels.id == id).first()


def update(data: UserSchemas, db: AsyncSession, id: int):
    user = db.query(UserModels).filter(UserModels.id == id).first()
    user.name = data.name

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def remove(db: AsyncSession, id: int):
    user = db.query(UserModels).filter(UserModels.id == id).delete()

    db.commit()

    return user
