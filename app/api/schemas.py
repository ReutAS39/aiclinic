from typing import Annotated
from pydantic import BaseModel


class CreateSchedule(BaseModel):
    doctors_stuff: str
    frequency: int
    duration: int
    recipient_id: int