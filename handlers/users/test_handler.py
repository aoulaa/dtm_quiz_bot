from aiogram import types

from keyboards.inline.in_buttons import present_buttons
from loader import dp


@dp.message_handler(text='Present simple')
async def send_present_q(message: types.Message):
    await message.answer('Present simple', reply_markup=present_buttons)
