import logging

from src.bot.engines import Engine, Transaction
from src.bot.repositories import UserRepository

logger = logging.getLogger(__name__)


class UserService:
    def __init__(
        self,
        user_repository: UserRepository = UserRepository(),
        transaction: Transaction = Transaction(Engine()),
    ):
        self.transaction = transaction
        self.user_repository = user_repository

    async def create_or_update(
        self,
        *,
        external_id: int,
        full_name: str,
    ) -> bool:
        async with self.transaction:
            result = await self.user_repository.create_or_update(
                external_id=external_id,
                full_name=full_name,
            )
            if not result:
                return False
            return True
