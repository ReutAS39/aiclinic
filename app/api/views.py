from typing import Annotated

from fastapi import APIRouter, Path

from app.api import crud
from app.api.schemas import CreateSchedule


router = APIRouter()


@router.get('/schedules')
def get_schedules_by_user_id(user_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    pass


@router.get('/schedule')
def get_day_schedule(user_id: int, schedule_id):
    pass


@router.get('next_takings')
def get_next_takings(user_id):
    pass

@router.post('/schedule')
def create_schedule(schedule: CreateSchedule):
    return crud.create_schedule(schedule=schedule)


# class ScheduleSchema(BaseModel):
#     id: int
#     pass



