from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)


class Schedules(Base):
    __tablename__ = 'schedules'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    doctors_stuff: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(String, nullable=False)
    duration = Mapped[int] = mapped_column( Integer, nullable=False)
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
