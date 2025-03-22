from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ScheduleBase(BaseModel):
    doctors_stuff: str = Field(max_length=20)
    frequency: int = Field(ge=1, le=24)
    duration: int = Field(ge=0)
    user_id: int = Field(ge=0)


class CreateScheduleSchema(ScheduleBase):
    pass


class ScheduleSchema(ScheduleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    add_in: datetime


class DayScheduleSchema(ScheduleSchema):
    model_config = ConfigDict(from_attributes=True)
    day_schedule: dict
