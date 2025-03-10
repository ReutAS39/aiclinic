from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from app.core.base import Base
from app.api.views import router as api_router

from app.core.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
