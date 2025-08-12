from typing import Optional
import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from backend.utils.database import Base


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[Optional[str]]
    last_name: Mapped[str]
    name: Mapped[str]
    nationality: Mapped[Optional[str]] = mapped_column(String(3))
    date_of_birth: Mapped[Optional[datetime.date]]
    sub_position: Mapped[Optional[str]] = mapped_column(String(3))
    position: Mapped[Optional[str]] = mapped_column(String(2))

    def __repr__(self):
        return f"{self.id}: {self.name} from {self.nationality} ({self.sub_position})"
