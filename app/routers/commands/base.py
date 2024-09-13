from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils import markdown

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Hello, {markdown.hbold(message.from_user.full_name)}!')
