from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.models.base import Base


class User(Base):
    __tablename__ = 'dictionaries'  # noqa

    external_id: Mapped[int] = mapped_column(
        VARCHAR,
        nullable=False,
    )
    full_name: Mapped[str] = mapped_column(
        VARCHAR,
        nullable=False,
    )
