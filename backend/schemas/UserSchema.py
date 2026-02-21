from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserReadSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
