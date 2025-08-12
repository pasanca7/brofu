from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.Game import Level


async def get_levels(db: AsyncSession) -> list[Level]:
    levels = await db.execute(select(Level))
    return levels.scalars().all()


async def get_level_by_id(db: AsyncSession, level_id: int) -> Level | None:
    level = await db.execute(select(Level).where(Level.id == level_id))
    return level.scalar_one_or_none()
