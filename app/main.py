from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI

from pydantic import BaseModel
from app.api.router_page import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with engine.be
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get('/', summary='приветствие')
def get_hello():
    return 'Hello world!!!'

@app.get('/schedules')
def get_schedules(user_id: int):
    pass


@app.get('/schedule')
def get_day_schedule(user_id: int, schedule_id):
    pass


@app.get('next_takings')
def get_next_takings(user_id):
    pass

class NewSchedule(BaseModel):
    pass


class ScheduleSchema(BaseModel):
    id: int
    pass


@app.post('/schedule')
def add_schedule(data: ScheduleSchema):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


