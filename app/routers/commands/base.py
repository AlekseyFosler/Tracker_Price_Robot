from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f'Hello, {markdown.hbold(message.from_user.full_name)}!\nThis command is under development.'
    )


@router.message(Command('info'))
async def handle_info(message: types.Message):
    await message.answer(
        text=f'Hello, {markdown.hbold(message.from_user.full_name)}!\nThis command is under development.'
    )


@router.message(Command('help'))
async def handle_help(message: types.Message):
    await message.answer(
        text=f'Hello, {markdown.hbold(message.from_user.full_name)}!\nThis command is under development.'
    )
