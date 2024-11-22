from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    if message.from_user:
        full_name = message.from_user.full_name
    else:
        full_name = 'None'
    await message.answer(text=f'Hello, {markdown.hbold(full_name)}!\nThis command is under development.')


@router.message(Command('info'))
async def handle_info(message: types.Message):
    if message.from_user:
        full_name = message.from_user.full_name
    else:
        full_name = 'None'
    await message.answer(text=f'Hello, {markdown.hbold(full_name)}!\nThis command is under development.')


@router.message(Command('help'))
async def handle_help(message: types.Message):
    if message.from_user:
        full_name = message.from_user.full_name
    else:
        full_name = 'None'
    await message.answer(text=f'Hello, {markdown.hbold(full_name)}!\nThis command is under development.')