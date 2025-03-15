from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ScheduleBase(BaseModel):
    doctors_stuff: str
    frequency: int
    duration: int
    user_id: int
    add_in: datetime

class CreateSchedule(ScheduleBase):
    pass


class Schedule(ScheduleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class Schedulezzz(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    doctors_stuff: str

class UserBase(BaseModel):
    name: str

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class CreateUser(UserBase):
    pass