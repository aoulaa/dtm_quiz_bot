

from aiogram import types

from keyboards.default.main_buttons import rating_buttons

from loader import dp


from utils.db_api import commands


@dp.message_handler(text='📊 Рейтинг')
async def get_to_ratings(msg: types.Message):
    text = """Это рейтинг игроков. 

Выполняй задания каждый день и получай рейтинговые очки!

Чтобы перейти в лигу выше нужно набрать минимум очков для перехода и войти в топ 3 игроков лиги.

Минимумы очков:
🥉 ->🥈 500
🥈 ->🥇 1000
🥇 ->💎 1900

Здесь ты можешь увидеть на каком ты месте и в какой лиге сейчас:"""
    await msg.answer(text, reply_markup=rating_buttons)


@dp.message_handler(text='🕴 Мой рейтинг')
async def get_my_rating(msg: types.Message):
    id = msg.from_user.id
    users = await commands.select_all_users()
    text = await my_rating(users, id)
    await msg.answer(text)


@dp.message_handler(text='🌎 Топ 10')
async def get_all_rating(msg: types.Message):
    users = await commands.select_all_users()
    text = await all_ratings(users)
    await msg.answer(text)


# counting ratings
async def my_rating(users, user_id):
    text = ''
    for num, usr in enumerate(users, 1):
        if usr.id == user_id:
            text += f'{num}) {usr.name} {usr.rating}💎\n'
    return text


async def all_ratings(users):
    text = ''

    for num, usr in enumerate(users, 1):
        text += f'{num}) {usr.name} {usr.rating}💎\n'
        if num == 10:
            return text
