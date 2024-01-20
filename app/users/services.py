from app.users import UserModels
from app.users import UserSchemas

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional


async def create_user(data: UserSchemas, db: AsyncSession) -> Optional[UserModels]:
    user = UserModels(**data.model_dump())

    try:
        db.add(user)
        await db.commit()
        await db.refresh(user)
    except Exception as e:
        print(e)

    return user


async def get_user(user_id: int, db: AsyncSession) -> Optional[UserModels]:
    user = await db.get(UserModels, user_id)

    return user


async def update(user_id: int, data: UserSchemas, db: AsyncSession) -> Optional[UserModels]:
    user = await get_user(user_id, db)
    user.name = data.name

    await db.commit()
    await db.refresh(user)

    return user


async def remove(user_id: int, db: AsyncSession) -> Optional[UserModels | dict]:
    user = await get_user(user_id, db)

    await db.delete(user)
    await db.commit()

    return {
        'result': 'deleted'
    }
