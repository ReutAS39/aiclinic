
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.api import crud
from app.api.schemas import  User, CreateUser, CreateSchedule, Schedule

router = APIRouter()


@router.get('/schedules/{user_id}', response_model=Schedule)
async def get_schedules_by_user_id(
        user_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    schedule = await crud.get_schedules_by_user_id(session=session, user_id=user_id)
    if schedule is not None:
        return schedule
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'schedule for user {user_id} not found!'
    )

@router.post('/schedule/', response_model=Schedule)
async def create_schedule(
        schedule_in: CreateSchedule,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_schedule(session=session, schedule_in=schedule_in)


# @router.get('/schedule')
# def get_day_schedule(user_id: int, schedule_id):
#     pass
#
#
# @router.get('next_takings')
# def get_next_takings(user_id):
#     pass

@router.post('/user/', response_model=User)
async def create_user(
        user_in: CreateUser,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)



