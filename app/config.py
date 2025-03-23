from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent
UPCOMING_PERIOD = 60



class Settings(BaseSettings):
    api_prefix: str = '/api'

    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'
    db_echo: bool = False


settings = Settings()
