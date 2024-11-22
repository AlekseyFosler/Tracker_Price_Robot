from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert

from src.bot.engines import Engine, Transaction
from src.bot.models import User


class UserRepository:
    def __init__(
        self,
        transaction: Transaction = Transaction(engine=Engine()),
    ):
        self.transaction: Transaction = transaction

    async def create_or_update_company(self, company_data: dict) -> User:
        stmt = (
            insert(User)
            .values(**company_data)
            .on_conflict_do_update(
                index_elements=User.__table__.primary_key.columns,
                set_={**company_data, User.updated_at: func.now()},
            )
            .returning(User)
        )
        return await self.transaction.execute(stmt)
