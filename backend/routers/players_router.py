from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.database import get_db
from backend.controllers import players_controller as controller
from backend.utils.logger import logger
from backend.schemas.PlayerSchema import PlayerSchema

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/search", response_model=List[PlayerSchema])
async def search_players_by_name(
    name: str = Query(..., min_length=1, description="Name to search"),
    db: AsyncSession = Depends(get_db),
):
    logger.info(f"Searching players by name: {name}")
    players = await controller.search_players_by_name(db, name)
    if not players:
        logger.warning(f"No players found with name: {name}")
    return players


@router.get("/{player_id}", response_model=PlayerSchema)
async def get_player_by_id(player_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Getting player with id {player_id}...")
    player = await controller.get_player_by_id(db, player_id)
    if player:
        logger.info(f"Player found: {player}")
        return player
    else:
        logger.error(f"Player with id {player_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
