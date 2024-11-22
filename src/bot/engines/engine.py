from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.bot.configs import settings


class Engine:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            url=str(settings.postgres.DSN),
            echo=False,
            echo_pool=False,
            pool_size=settings.postgres.POOL_SIZE,
            max_overflow=settings.postgres.MAX_OVERFLOW,
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )
