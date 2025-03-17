

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import UserOrm, ScheduleOrm
from app.api.schemas import CreateUserSchema, CreateScheduleSchema


# async def get_schedules_by_user_id(session: AsyncSession, user_id: int) -> Schedule | None:
#     # stmt = select(Schedule)
#     # result: Result = await session.execute(stmt)
#     # schedules = result.scalar().all()
#
#     # return list(schedules)
#     return await session.get(Schedule, user_id)


async def create_schedule(session: AsyncSession, schedule_in: CreateScheduleSchema) -> ScheduleOrm | None:
    schedule = ScheduleOrm(**schedule_in.model_dump())
    session.add(schedule)
    await session.commit()
    return schedule

async def get_schedules_id_by_user_id(session: AsyncSession, **filter_by) -> list[ScheduleOrm]:
    # stmt = select(Schedule).filter_by(recipient_id=recipient_id).order_by(Schedule.id)
    # result: Result = await session.execute(stmt)
    # schedules = result.scalars().all()

    query = select(ScheduleOrm).filter_by(**filter_by)
    result1: Result = await session.execute(query)
    schedules1 = result1.scalars().all()
    return list(schedules1)


async def get_schedule_for_user(session: AsyncSession, **filter_by):
    query = select(ScheduleOrm).filter_by(**filter_by)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    return list(schedules)




# async def create_user(session: AsyncSession, user_in: CreateUser) -> User | None:
#     user = User(**user_in.model_dump())
#     session.add(user)
#     await session.commit()
#     # await session.refresh(schedule)
#     return user