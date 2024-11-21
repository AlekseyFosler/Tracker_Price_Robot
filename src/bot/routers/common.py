from aiogram import Router, types

router = Router(name=__name__)


@router.message()
async def reply_all_message(message: types.Message):
    await message.reply(text='Something new 🙂')
