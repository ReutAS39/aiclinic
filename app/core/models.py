from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()[:-5]}s"

    id: Mapped[int] = mapped_column(primary_key=True)

    # created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

class UserModel(Base):

    name: Mapped[str]


class ScheduleModel(Base):

    doctors_stuff: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(Integer, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    add_in: Mapped[datetime] = mapped_column(server_default=func.now())


