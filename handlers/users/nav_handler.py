from aiogram import types

from data.dict_pack import main_topic, dict_nov_bar
from keyboards.default.main_buttons import genrate_button
from loader import dp


@dp.message_handler(text='🧠 Заниматься')
async def navigation(msg: types.Message):
    await msg.answer('выбори тему и начни практиковатся',
                     reply_markup=genrate_button(main_topic))


@dp.message_handler(text=dict_nov_bar)
async def dict_nov(msg: types.Message):
    await msg.answer('welcome bro',
                     reply_markup=genrate_button(dict_nov_bar[msg.text]))
