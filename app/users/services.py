from app.users import UserModels
from app.users import UserSchemas

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional

from fastapi import HTTPException


async def create_user(data: UserSchemas, db: AsyncSession) -> Optional[UserModels]:
    user = UserModels(**data.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(user_id: int, db: AsyncSession) -> Optional[UserModels]:
    user = await db.get(UserModels, user_id)
    if not user:
        raise HTTPException(404, 'User not found')
    return user


async def update(user_id: int, data: UserSchemas, db: AsyncSession) -> Optional[UserModels]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'User not found')
    user.name = data.name
    await db.commit()
    await db.refresh(user)
    return user


async def remove(user_id: int, db: AsyncSession) -> Optional[UserModels | dict]:
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(404, 'Item not found')
    await db.delete(user)
    await db.commit()
    return {
        'message': 'deleted'
    }
