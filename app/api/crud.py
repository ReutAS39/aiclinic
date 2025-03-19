from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import UserOrm, ScheduleOrm
from app.core.utils import freq
from app.api.schemas import CreateUserSchema, CreateScheduleSchema


async def create_schedule(session: AsyncSession, schedule_in: CreateScheduleSchema) -> int:
    schedule = ScheduleOrm(**schedule_in.model_dump())
    session.add(schedule)
    await session.commit()
    return schedule.id


async def get_schedules_id_by_user_id(session: AsyncSession, user_id: int) -> list[int]:
    schedules_ids = []
    query = select(ScheduleOrm).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    for schedule in schedules:
        schedules_ids.append(schedule.id)
    return schedules_ids


async def get_schedule_for_user(session: AsyncSession, user_id: int, schedule_id: int, ) -> ScheduleOrm:
    query = select(ScheduleOrm).where(ScheduleOrm.id == schedule_id, ScheduleOrm.user_id == user_id)
    result: Result = await session.execute(query)
    schedule = result.scalar_one_or_none()
    raspisanie = freq(schedule.frequency)
    print('!!!!!!')
    print(raspisanie)
    return schedule


# async def create_user(session: AsyncSession, user_in: CreateUser) -> User | None:
#     user = User(**user_in.model_dump())
#     session.add(user)
#     await session.commit()
#     # await session.refresh(schedule)
#     return user
