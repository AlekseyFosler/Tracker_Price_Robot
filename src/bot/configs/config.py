from logging import INFO

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='POSTGRES_')

    DSN: PostgresDsn = PostgresDsn(
        'postgresql+asyncpg://admin:admin@tracker_price_robot_postgres:5432/tracker_price_robot_postgres'
    )
    POOL_SIZE: int = 20
    MAX_OVERFLOW: int = 5
    MAX_TIME: int = 2
    MAX_TRIES: int = 3


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    bot_token: str = 'bot_token'
    logging_level: int = INFO

    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
