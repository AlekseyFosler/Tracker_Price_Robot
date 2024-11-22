import logging

from aiogram import Router, types
from aiogram.filters import Command

from src.bot.parsers import WildberriesParser

router = Router(name=__name__)
logger = logging.getLogger(__name__)
Wildberries_Parser = WildberriesParser()


@router.message(Command('add'))
async def handle_info(message: types.Message):
    logger.debug(message.text)
    product = Wildberries_Parser.parse_product(message.text.replace('/add ', ''))
    logger.info(product)
    await message.answer(str(product))
