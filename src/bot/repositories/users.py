from sqlalchemy import Result, func
from sqlalchemy.dialects.postgresql import insert

from src.bot.engines import Engine, Transaction
from src.bot.models import User


class UserRepository:
    def __init__(
        self,
        transaction: Transaction = Transaction(engine=Engine()),
    ):
        self.transaction: Transaction = transaction

    async def create_or_update(
        self,
        external_id: int,
        full_name: str,
    ) -> User:
        stmt = (
            insert(User)
            .values(
                {
                    User.external_id.name: external_id,
                    User.full_name.name: full_name,
                }
            )
            .on_conflict_do_update(
                index_elements=User.__table__.primary_key.columns,
                set_={
                    User.external_id.name: external_id,
                    User.full_name.name: full_name,
                    User.updated_at: func.now(),
                },
            )
            .returning(User)
        )
        cursor: Result = await self.transaction.execute(stmt)
        return cursor.scalar_one()
