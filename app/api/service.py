from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ScheduleModel
from app.utils import ScheduleManager
from app.api.schemas import CreateScheduleSchema


async def create_schedule(session: AsyncSession, schedule_in: CreateScheduleSchema) -> int:
    schedule = ScheduleModel(**schedule_in.model_dump())
    session.add(schedule)
    try:
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise e
    return schedule.id


async def get_schedules_ids(session: AsyncSession, user_id: int) -> list[int]:
    query = select(ScheduleModel).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    if schedules:
        return [schedule.id for schedule in schedules]


async def get_ext_schedule(session: AsyncSession, user_id: int, schedule_id: int, ) -> dict | None:
    query = select(ScheduleModel).where(ScheduleModel.id == schedule_id, ScheduleModel.user_id == user_id)
    result: Result = await session.execute(query)
    schedule = result.scalar_one_or_none()
    if schedule is not None:
        schedule_dict = jsonable_encoder(schedule)
        schedule_dict['day_schedule'] = ScheduleManager.get_day_schedule(schedule.frequency)
        return schedule_dict


async def get_next_takings(session: AsyncSession, user_id: int) -> dict:
    query = select(ScheduleModel).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    all_schedules = {}
    for schedule in schedules:
        all_schedules[f'{schedule.doctors_stuff}'] = ScheduleManager.get_day_schedule(schedule.frequency)
    next_takings = ScheduleManager.get_next_takings(all_schedules)
    if next_takings:
        return next_takings
