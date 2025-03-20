
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from app.db_helper import db_helper, SessionDep
from app.api import service
from app.api.schemas import CreateScheduleSchema, DayScheduleSchema

# from app.api.schemas import UserSchema, CreateUserSchema

router = APIRouter(tags=['Schedules'])


@router.post('/schedule/', summary='Создание расписания')
async def create_schedule(
        schedule_in: CreateScheduleSchema,
        session: SessionDep,
) -> int:
    try:
        return await service.create_schedule(session=session, schedule_in=schedule_in)
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка при добавлении расписания.")


@router.get(
    '/schedules/user_id={user_id}',
    summary='Retrieves a list of schedules for the specified user')
async def get_schedules_id_by_user_id(
        user_id: int,
        session: SessionDep,
) -> list[int]:
    schedules = await service.get_schedules_id_by_user_id(session=session, user_id=user_id)
    if len(schedules):
        return schedules
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'schedules for user {user_id}  not found!'
    )


@router.get(
    '/schedule/user_id={user_id}&schedule_id={schedule_id}',
    summary='Данные о выбранном расписании с рассчитанным графиком приёмов на день')
async def get_schedule_for_user(
        user_id: int,
        schedule_id: int,
        session: SessionDep,
        # session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> DayScheduleSchema:
    schedule = await service.get_schedule_for_user(session=session, user_id=user_id, schedule_id=schedule_id)
    return schedule


@router.get(
    '/next_takings',
    summary='Возвращает данные о таблетках, которые необходимо принять в ближайшие период')
async def get_next_takings(
        user_id: int,
        session: SessionDep,
) -> dict:
    schedules = await service.get_next_taking(session=session, user_id=user_id)
    if schedules is not None:

        return schedules
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'schedule for user  not found!'
)



# @router.post('/user/', response_model=User)
# async def create_user(
#         user_in: CreateUser,
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.create_user(session=session, user_in=user_in)
#

