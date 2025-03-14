

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import User, Schedule
from app.api.schemas import CreateUser, CreateSchedule


# async def get_schedules_by_user_id(session: AsyncSession, user_id: int) -> Schedule | None:
#     # stmt = select(Schedule)
#     # result: Result = await session.execute(stmt)
#     # schedules = result.scalar().all()
#
#     # return list(schedules)
#     return await session.get(Schedule, user_id)

async def get_schedules_by_user_id(session: AsyncSession, user_id: int) -> list[Schedule]:
    stmt = select(Schedule).filter_by(id=user_id)
    result: Result = await session.execute(stmt)
    schedules = result.scalar().all()

    return list(schedules)



async def create_schedule(session: AsyncSession, schedule_in: CreateSchedule) -> Schedule | None:
    schedule = Schedule(**schedule_in.model_dump())
    session.add(schedule)
    await session.commit()
    # await session.refresh(schedule)
    return schedule


async def create_user(session: AsyncSession, user_in: CreateUser) -> User | None:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(schedule)
    return user