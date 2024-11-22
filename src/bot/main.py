import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.bot.configs import settings
from src.bot.routers import router as main_router


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=settings.logging_level)
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('@Tracker_Price_Robot is Off')
