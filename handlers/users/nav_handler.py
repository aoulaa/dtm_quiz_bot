from aiogram import types

from data.dict_pack import main_topic, dict_nov_bar
from keyboards.default.main_buttons import genrate_button
from loader import dp, _


@dp.message_handler(text=_('🧠 Заниматься'))
async def navigation(msg: types.Message):
    await msg.answer(_('Выбери тему и начни попрактиковаться'),
                     reply_markup=genrate_button(main_topic, False))


@dp.message_handler(text=dict_nov_bar)
async def dict_nov(msg: types.Message):
    await msg.answer(_('Выбери выбери тему'),
                     reply_markup=genrate_button(dict_nov_bar[msg.text], False))
