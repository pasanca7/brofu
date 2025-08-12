from typing import Optional, List
from pydantic import BaseModel

from backend.schemas.PlayerSchema import PlayerBasicSchema


class LevelBasicSchema(BaseModel):
    id: int
    team: str
    season: str
    logo_url: Optional[str] = None

    class Config:
        from_attributes = True


class LevelSchema(LevelBasicSchema):
    players: List[PlayerBasicSchema] = []
