from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base import Base


class UserOrm(Base):

    name: Mapped[str]


class ScheduleOrm(Base):

    doctors_stuff: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(Integer, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("userorms.id"))
    add_in: Mapped[datetime] = mapped_column(server_default=func.now())


