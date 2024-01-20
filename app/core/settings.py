from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath

from functools import lru_cache

from pathlib import Path

from sqlalchemy import URL


class DbSettings(BaseSettings):
    root_dir: DirectoryPath = Path(__file__).parent.parent.parent
    model_config = SettingsConfigDict(
        env_file=f'{root_dir}/.env',
        env_file_encoding='utf-8',
    )
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    def create_url(self):
        url_obj = URL.create(
            'postgresql+psycopg',
            username=self.DB_USER,
            password=self.DB_PASS,
            database=self.DB_NAME,
            host=self.DB_HOST,
            port=self.DB_PORT
        )
        return url_obj


class Settings(BaseSettings):
    db: DbSettings = DbSettings()


@lru_cache(typed=True)
def get_settings() -> Settings:
    return Settings()
