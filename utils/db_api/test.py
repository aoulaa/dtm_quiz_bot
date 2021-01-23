import asyncio

from data import config
from utils.db_api import commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await commands.add_question("present_simple", "i ... from Russia", 'am', 'is,are,has')
    await commands.add_question("present_simple", "you ... my friend", 'are', 'is,am,have')

    # await commands.add_user(2, 'name')
    # await commands.add_user_with_id(15, )
    # await commands.add_user_with_id(2, )
    # await commands.add_user_with_id( 3, )
    # await commands.add_user_with_id( )
    r = await commands.select_all_users()


    # print(f'hey {r[0].questions_ids}')
    # await commands.add_question(3, "1")
    # await commands.add_question(4, "1")
    # await commands.add_question(5, "John")
    print("Готово")
    # quest = await commands.select_question_by_topic('present_simple')
    # print(f'questions by topics:{quest}')

    # questions = await commands.select_all_question()
    # print(f"Получил всех пользователей: {questions}")

    # count_users = await commands.count_users()
    # print(f"Всего пользователей: {count_users}")
    #
    # user = await commands.select_user(id=5)
    # print(f"Получил пользователя: {user}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
