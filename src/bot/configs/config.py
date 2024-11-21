from logging import INFO

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    bot_token: str = 'bot_token'
    logging_level: int = INFO


settings = Settings()
