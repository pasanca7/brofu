from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.Player import Player


async def get_player_by_id(db: AsyncSession, player_id: int) -> Player | None:
    player = await db.execute(select(Player).where(Player.id == player_id))
    return player.scalar_one_or_none()


async def search_players_by_name(db: AsyncSession, name: str):
    stmt = select(Player).where(
        func.unaccent(func.lower(Player.name)).ilike(f"%{name.lower()}%")
    )
    result = await db.execute(stmt)
    return result.scalars().all()
