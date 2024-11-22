import backoff
from asyncpg.exceptions import TooManyConnectionsError  # type: ignore
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.configs import settings
from src.bot.engines.engine import Engine


class Transaction:
    def __init__(self, engine: Engine):
        self._engine = engine
        self._session: AsyncSession | None = None

    async def __aenter__(self):
        self._session = self._engine.async_session()

    async def __aexit__(self, exc_type, *args):
        if self._session:
            await self.rollback()
            await self._session.close()
            self._session = None

    async def commit(self):
        if self._session:
            await self._session.commit()

    async def rollback(self):
        if self._session:
            await self._session.rollback()

    @backoff.on_exception(
        backoff.expo,
        TooManyConnectionsError,
        max_time=settings.postgres.MAX_TIME,
        max_tries=settings.postgres.MAX_TRIES,
    )
    async def execute(self, *args, **kwargs) -> Result:
        if self._session:
            return await self._session.execute(*args, **kwargs)
        raise
