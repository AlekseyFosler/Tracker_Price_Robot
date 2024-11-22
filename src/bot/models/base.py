import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import BIGINT, INTEGER, TIMESTAMP, String, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        int: BIGINT,
        datetime: TIMESTAMP(timezone=False),
        str: String(),
        dict[str, Any]: JSONB,
        list[UUID]: ARRAY(UUID()),
        list[str]: ARRAY(String()),
        list[int]: ARRAY(INTEGER),
    }

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
    )
