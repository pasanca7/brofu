from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.User import User


async def get_user_by_usename(db: AsyncSession, username: str) -> User:
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()
