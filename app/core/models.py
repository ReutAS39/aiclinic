from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base import Base


class User(Base):

    name: Mapped[str]


class Schedule(Base):

    doctors_stuff: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(String, nullable=False)
    duration : Mapped[int] = mapped_column(Integer, nullable=False)
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    add_in: Mapped[datetime] = mapped_column(server_default=func.now())


