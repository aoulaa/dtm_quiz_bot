import json

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.main_buttons import main_b
from loader import dp
from utils.db_api import commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id not in [usr.id for usr in await commands.select_all_users()]:
        stats = json.dumps({})
        await commands.add_user(message.from_user.id, message.from_user.full_name, stats)
        await message.answer(f'Привет, {message.from_user.full_name}!\n'
                             f'Ты у нас первый раз!\n'
                             f'Сейчас будем учить английский',
                             reply_markup=main_b)
        return
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Сейчас будем учить английский', reply_markup = main_b)
