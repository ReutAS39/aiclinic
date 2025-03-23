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


async def get_schedules_id_by_user_id(session: AsyncSession, user_id: int) -> list[int]:
    try:
        query = select(ScheduleModel).filter_by(user_id=user_id)
        result: Result = await session.execute(query)
        schedules = result.scalars().all()
        if schedules:
            return [schedule.id for schedule in schedules]
    except SQLAlchemyError as e:
        return []


async def get_schedule_for_user(session: AsyncSession, user_id: int, schedule_id: int, ) -> dict | None:
    query = select(ScheduleModel).where(ScheduleModel.id == schedule_id, ScheduleModel.user_id == user_id)
    result: Result = await session.execute(query)
    schedule = result.scalar_one_or_none()
    if schedule is not None:
        print(schedule)
        json_compatible_schedule_data = jsonable_encoder(schedule)
        print(type(json_compatible_schedule_data))
        day_schedule = await ScheduleManager.get_day_schedule(schedule.frequency) #session execute TODO
        json_compatible_schedule_data['day_schedule'] = day_schedule

        return json_compatible_schedule_data

    return schedule


async def get_next_taking(session: AsyncSession, user_id: int) -> dict:
    test = {}
    query = select(ScheduleModel).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    for schedule in schedules:
        test[f'{schedule.doctors_stuff}'] = await ScheduleManager.get_day_schedule(schedule.frequency)
    a = ScheduleManager(test=test).get_next_taking()

    return a
