from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ScheduleBase(BaseModel):
    doctors_stuff: str = Field(max_length=20)
    frequency: int = Field(ge=1, le=24)
    duration: int = Field(ge=0)
    user_id: int



class CreateScheduleSchema(ScheduleBase):
    pass


class ScheduleSchema(ScheduleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    add_in: datetime


class DayScheduleSchema(ScheduleSchema):
    day_schedule: dict

# class UserBase(BaseModel):
#     name: str
#
#
# class UserSchema(UserBase):
#     model_config = ConfigDict(from_attributes=True)
#     id: int
#
#
# class CreateUserSchema(UserBase):
#     pass
