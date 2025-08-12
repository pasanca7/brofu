from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.schemas.GameSchema import LevelSchema, LevelBasicSchema
from backend.utils.logger import logger
from backend.utils.database import get_db
from backend.controllers import game_controller as controller


router = APIRouter(prefix="/game", tags=["Game"])


@router.get("/levels", response_model=list[LevelBasicSchema])
async def get_levels(db: AsyncSession = Depends(get_db)):
    logger.info("Getting all levels from database")
    levels = await controller.get_levels(db)
    return levels


@router.get("/level/{level_id}", response_model=LevelSchema)
async def get_level(level_id: int, db: AsyncSession = Depends(get_db)):
    logger.info(f"Getting level {level_id} from database")
    level = await controller.get_level_by_id(db, level_id)
    if level:
        return level
    else:
        logger.error(f"Level with id {level_id} not found")
        raise HTTPException(status_code=404, detail="Level not found")
