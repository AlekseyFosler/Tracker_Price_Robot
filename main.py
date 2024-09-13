import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import settings


async def main():
    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
