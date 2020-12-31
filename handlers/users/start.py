from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_buttons import main_b
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=main_b)
