from aiogram import types

from data.config import contributor
from keyboards.default.main_buttons import rating_buttons

from loader import dp, _

from utils.db_api import commands


@dp.message_handler(text=_('📊 Рейтинг'))
async def get_to_ratings(msg: types.Message):
    text = _('Это рейтинг игроков.\n'
             'Выполняй тесты каждый день и получай рейтинговые очки!\n\n'
             'Здесь ты можешь увидеть на каком ты месте и в какой лиге сейчас:')

    await msg.answer(text, reply_markup=rating_buttons)


@dp.message_handler(text=_('🕴 Мой рейтинг'))
async def get_my_rating(msg: types.Message):
    id = msg.from_user.id
    users = await commands.select_all_users()
    text = await my_rating(users, id)
    await msg.answer(text)


@dp.message_handler(text=_('🌎 Топ 10'))
async def get_all_rating(msg: types.Message):
    users = await commands.select_all_users()
    text = await all_ratings(users)
    await msg.answer(text)


# counting ratings of one user
async def my_rating(users, user_id):
    text = ''
    for num, usr in enumerate(users, 1):
        if usr.id == user_id:
            text += f'{num}) {usr.name} <b>{usr.rating}</b> 💎\n'
    return text


# counting ratings of many users
async def all_ratings(users):
    text = ''
    for num, usr in enumerate(users, 1):
        if num <= 10:
            text += f'{num}) {usr.name} <b>{usr.rating}</b> 💎\n'
    return text


# admin ratings
@dp.message_handler(text='Rating 📊')
async def get_all_rating_admins(msg: types.Message):
    users = await commands.select_all_admins()
    text = await all_ratings_admin(users)
    await msg.answer(text)


async def all_ratings_admin(users):
    text = ''
    for num, usr in enumerate(users, 1):
        if usr.id in contributor:
            text += f'{num}) {usr.name} added <b>{usr.admin_stats}</b> questions.\n'
    return text
