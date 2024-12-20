__all__ = ('router',)

from aiogram import Router

from .base import router as base_commands_router
from .products import router as products_commands_router

router = Router(name=__name__)

router.include_routers(
    base_commands_router,
    products_commands_router,
)
