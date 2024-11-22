from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.models.base import Base


class User(Base):
    __tablename__ = 'dictionaries'  # noqa

    login: Mapped[str] = mapped_column(
        VARCHAR,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(
        VARCHAR,
        nullable=False,
    )
