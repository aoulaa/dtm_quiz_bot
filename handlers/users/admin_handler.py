from loader import dp
from aiogram import types



@dp.message_handler(commands='add_question')
async def add_question(msg: types.Message):
    await msg.answer('send the ')