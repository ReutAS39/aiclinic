from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import ScheduleModel
from app.core.utils import freq
from app.api.schemas import CreateScheduleSchema

# from app.core.models import UserModel
# from app.api.schemas import CreateUserSchema


async def create_schedule(session: AsyncSession, schedule_in: CreateScheduleSchema) -> int:
    schedule = ScheduleModel(**schedule_in.model_dump())
    session.add(schedule)
    try:
        await session.commit()
    except SQLAlchemyError as e:
        raise e
    return schedule.id


async def get_schedules_id_by_user_id(session: AsyncSession, user_id: int) -> list[int]:
    schedules_ids = []
    query = select(ScheduleModel).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    for schedule in schedules:
        schedules_ids.append(schedule.id)
    return schedules_ids


async def get_schedule_for_user(session: AsyncSession, user_id: int, schedule_id: int, ) -> dict:
    query = select(ScheduleModel).where(ScheduleModel.id == schedule_id, ScheduleModel.user_id == user_id)
    result: Result = await session.execute(query)
    schedule = result.scalar_one_or_none()
    day_schedule = freq(schedule.frequency)
    json_compatible_schedule_data = jsonable_encoder(schedule)
    json_compatible_schedule_data['day_schedule'] = day_schedule


    return json_compatible_schedule_data


async def get_next_taking(session: AsyncSession, user_id: int) -> dict:
    test = {}
    query = select(ScheduleModel).filter_by(user_id=user_id)
    result: Result = await session.execute(query)
    schedules = result.scalars().all()
    for schedule in schedules:
        test[f'{schedule.doctors_stuff}'] = freq(schedule.frequency)


    return test







# async def create_user(session: AsyncSession, user_in: CreateUser) -> User | None:
#     user = User(**user_in.model_dump())
#     session.add(user)
#     await session.commit()
#     # await session.refresh(schedule)
#     return user
