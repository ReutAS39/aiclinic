from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.database import SessionDep
from app.api import service
from app.api.schemas import CreateScheduleSchema, DayScheduleSchema

router = APIRouter(tags=['Schedules'])


@router.post('/schedule', summary='Создание расписания')
async def create_schedule(
        schedule_in: CreateScheduleSchema,
        session: SessionDep,
) -> int:
    """
    Создание расписания со следующими параметрами:

    - **doctors_stuff**: Наименование лекарства
    - **frequency**: Периодичность приёмов за день, количество раз
    - **duration**: Продолжительность лечения, дней (при 0 неограниченная)
    - **user_id**: Идентификатор пользователя (у каждого зверя есть медицинский полис, будем считать,
    что его номер это  и есть идентификатор пользователя)
    """
    try:
        return await service.create_schedule(session=session, schedule_in=schedule_in)
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при добавлении расписания - {e}"
        )


@router.get(
    '/schedules',
    summary='Возвращает список идентификаторов существующих расписаний для указанного пользователя')
async def get_schedules_ids(
        user_id: int,
        session: SessionDep,
) -> list[int]:
    schedules = await service.get_schedules_ids(session=session, user_id=user_id)
    if schedules:
        return schedules
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Расписаний для пользовтеля {user_id} не найдено!'
    )


@router.get(
    '/schedule',
    summary='Возвращает данные о выбранном расписании с рассчитанным графиком приёмов на день')
async def get_ext_schedule(
        user_id: int,
        schedule_id: int,
        session: SessionDep,
) -> DayScheduleSchema | dict:
    schedule = await service.get_ext_schedule(session=session, user_id=user_id, schedule_id=schedule_id)
    if schedule is not None:
        return schedule
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Расписание {schedule_id} для пользовтеля {user_id} не найдено!'
    )


@router.get(
    '/next_takings',
    summary='Возвращает данные о таблетках, которые необходимо принять в ближайшие период')
async def get_next_takings(
        user_id: int,
        session: SessionDep,
) -> dict:
    schedules = await service.get_next_takings(session=session, user_id=user_id)
    if schedules is not None:
        return schedules
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Расписаний не найдено!'
    )
