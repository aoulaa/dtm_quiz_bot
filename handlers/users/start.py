import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.dict_pack import main_topic, topic_for_admins
from keyboards.default.main_buttons import main_menu_buttons, admin_button, genrate_button
from keyboards.inline.in_buttons import languages_markup
from loader import dp, _
from states import Admin
from utils.db_api import commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id not in [usr.id for usr in await commands.select_all_users()]:
        stats = json.dumps({})
        rating = 0
        await commands.add_user(message.from_user.id, message.from_user.full_name, stats, rating)
        await message.answer(f'Привет, {message.from_user.full_name}!\n'
                             f'Ты у нас первый раз!\n'
                             f'Сейчас будем учить английский',
                             reply_markup=languages_markup)
        return
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Сейчас будем учить английский', reply_markup=main_menu_buttons)


@dp.message_handler(text=_('назад'), state="*")
async def get_to_tests(msg: types.Message, state: FSMContext):
    await msg.answer(_('вы в главном меню'),
                     reply_markup=main_menu_buttons)
    await state.finish()


@dp.message_handler(text='back', state="*")
async def go_back_to_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('back to topics',
                         reply_markup=genrate_button(topic_for_admins, False))
    await Admin.add_topic.set()


@dp.message_handler(text='bаck', state="*")
async def go_back_to_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('you are in main admin',
                         reply_markup=admin_button)


@dp.message_handler(text='🔙back', state="*")
async def back_to_main_topic(msg: types.Message, state: FSMContext):
    await state.reset_state()
    await msg.answer('выибирите другю тему',
                     reply_markup=genrate_button(main_topic, False))
