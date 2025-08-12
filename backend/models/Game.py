from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import String, Table, Column, ForeignKey, Integer

from backend.utils.database import Base

level_players = Table(
    "level_players",
    Base.metadata,
    Column("level_id", ForeignKey("levels.id", ondelete="CASCADE"), primary_key=True),
    Column("player_id", ForeignKey("players.id", ondelete="CASCADE"), primary_key=True),
)


class Level(Base):
    __tablename__ = "levels"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team: Mapped[str] = mapped_column(String(255), nullable=False)
    season: Mapped[str] = mapped_column(String(255), nullable=False)
    logo_url: Mapped[str] = mapped_column(String(255), nullable=False)

    players: Mapped[list["Player"]] = relationship(
        "Player", secondary=level_players, lazy="selectin"
    )
