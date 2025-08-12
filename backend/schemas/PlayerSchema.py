import datetime
from typing import Optional
from pydantic import BaseModel


class PlayerBasicSchema(BaseModel):
    id: int
    name: str
    nationality: Optional[str]
    position: Optional[str]
    sub_position: Optional[str]

    class Config:
        from_attributes = True


class PlayerSchema(PlayerBasicSchema):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[datetime.date]
