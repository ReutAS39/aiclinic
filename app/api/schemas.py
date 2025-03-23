from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ScheduleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    doctors_stuff: str = Field(max_length=20)
    frequency: int = Field(ge=1, le=24)
    duration: int = Field(ge=0)
    user_id: int = Field(ge=0)


class ScheduleSchema(ScheduleBase):
    id: int
    add_in: datetime


class CreateScheduleSchema(ScheduleBase):
    pass


class DayScheduleSchema(ScheduleSchema):
    day_schedule: dict
