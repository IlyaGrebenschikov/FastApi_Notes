from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath

from functools import lru_cache

from pathlib import Path


class DbSettings(BaseSettings):
    root_dir: DirectoryPath = Path(__file__).parent.parent.parent.parent
    model_config = SettingsConfigDict(
        env_file=f'{root_dir}/.env',
        env_file_encoding='utf-8',
    )
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_URL: str

    def db_url(self):
        return self.DB_URL.format(
            db_user=self.DB_USER,
            db_pass=self.DB_PASS,
            db_host=self.DB_HOST,
            db_port=self.DB_PORT,
            db_name=self.DB_NAME,
        )


class Settings(BaseSettings):
    db: DbSettings = DbSettings()


@lru_cache(typed=True)
def get_settings() -> Settings:
    return Settings()
