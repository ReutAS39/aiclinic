
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.api.rb import RBSchedule, RBSchedules
from app.core import db_helper
from app.api import crud
from app.api.schemas import User, CreateUser, CreateSchedule, Schedule, Schedulezzz

router = APIRouter()


@router.post('/schedule/', summary='Создание расписания')
async def create_schedule(
        schedule_in: CreateSchedule,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Schedulezzz:
    return await crud.create_schedule(session=session, schedule_in=schedule_in)

@router.get('/schedules/user_id={user_id}', summary='Cписок идентификаторов существующих расписаний для указанного пользователя')
async def get_schedules_id_by_user_id(
        request_body: RBSchedules = Depends(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Schedulezzz]:
    schedules = await crud.get_schedules_id_by_user_id(session=session, **request_body.to_dict())
    if schedules is not None:
        return schedules
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'schedule for user  not found!'
    )

@router.get('/schedule/user_id={user_id}&schedule_id={schedule_id}', summary='Данные о выбранном расписании с рассчитанным графиком приёмов на день')
async def get_schedule_for_user(
        request_body: RBSchedule = Depends(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Schedule]:
    schedule = await crud.get_schedule_for_user(session=session, **request_body.to_dict())
    return schedule


@router.get('next_takings', summary='Возвращает данные о таблетках, которые необходимо принять в ближайшие период')
async def get_next_takings(
        request_body: RBSchedules = Depends(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Schedulezzz]:
    schedules = await crud.get_schedules_id_by_user_id(session=session, **request_body.to_dict())
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


