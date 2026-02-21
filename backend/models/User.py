import uuid
import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum
from sqlalchemy.dialects.postgresql import UUID

from backend.utils.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    second_name: Mapped[str] = mapped_column(String(255), nullable=True)
