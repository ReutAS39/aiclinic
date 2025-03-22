from datetime import datetime

from sqlalchemy import String, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:

        return cls.__name__.replace('Model', 's').lower()

    id: Mapped[int] = mapped_column(primary_key=True)


class ScheduleModel(Base):

    doctors_stuff: Mapped[str] = mapped_column(String, nullable=False)
    frequency: Mapped[str] = mapped_column(Integer, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    add_in: Mapped[datetime] = mapped_column(server_default=func.now())
