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
    Create an item with all the information:

    - **doctors_stuff**: Наименование лекарства
    - **frequency**: Периодичность приёмов
    - **duration**: Продолжительность лечения
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
    '/schedule',
    summary='Возвращает данные о выбранном расписании с рассчитанным графиком приёмов на день')
async def get_schedule_for_user(
        user_id: int,
        schedule_id: int,
        session: SessionDep,
) -> DayScheduleSchema | dict:
    schedule = await service.get_schedule_for_user(session=session, user_id=user_id, schedule_id=schedule_id)
    if schedule is None:
        return {'message': f'Расписание №{schedule_id} для пользовтеля {user_id} не найдено!'}
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
