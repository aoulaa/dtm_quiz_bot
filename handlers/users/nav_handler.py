from aiogram import types

from data.dict_pack import dict_of_topics
from keyboards.default.main_buttons import generate_button
from loader import dp, _


@dp.message_handler(text=_('🧠 Заниматься'))
async def navigation(msg: types.Message):

    await msg.answer(_('Выбери тему и начни попрактиковаться'),
                     reply_markup=generate_button(dict_of_topics, False))

#
# @dp.message_handler(text=dict_nov_bar)
# async def dict_nov(msg: types.Message):
#     await msg.answer(_('Выбери тему'),
#                      reply_markup=generate_button(dict_nov_bar[msg.text], False))
