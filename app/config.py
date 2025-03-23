from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    DB_URL: str = f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'

    UPCOMING_PERIOD: int = 60


settings = Settings()
