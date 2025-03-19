from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ScheduleBase(BaseModel):
    doctors_stuff: str
    frequency: int
    duration: int
    user_id: int
    add_in: datetime


class CreateScheduleSchema(ScheduleBase):
    pass


class ScheduleSchema(ScheduleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserBase(BaseModel):
    name: str


class UserSchema(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CreateUserSchema(UserBase):
    pass
