from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from app.models import Base
from app.api.views import router as api_router
from app.config import settings

from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api_prefix)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
