# from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino, commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Чистим базу")
    await db.gino.drop_all()

    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()
    await commands.add_question(1, "present_simple", "i ... from Russia", 'am', 'is,are,has')
    await commands.add_question(2, "present_simple", "you ... my friend", 'are', 'is,am,have')
    await commands.add_question(3, "present_simple", "He ... my son", 'is', 'nor,are,has')
    await commands.add_question(4, "present_simple", "they ... working with me", 'are', 'is,am,have')
    await commands.add_question(5, "present_simple", "IT ... very good place to work and grow", 'is', 'are,am,have')
    await commands.add_question(6, "present_simple", "They ... selling things ", 'are', 'is,am,have')

    await commands.add_question(7, "past_simple", "i ... from Russia", 'was', 'is,are,has')
    await commands.add_question(8, "past_simple", "you ... my friend", 'were', 'is,am,have')
    await commands.add_question(9, "past_simple", "He ... my son", 'was', 'nor,are,has')
    await commands.add_question(10, "past_simple", "they ... working with me", 'were', 'is,am,have')
    await commands.add_question(11, "past_simple", "IT ... very good place to work and grow", 'was', 'are,am,have')
    await commands.add_question(12, "past_simple", "They ... selling things ", 'were', 'is,am,have')
    print("Готово")
    await on_startup_notify(dp)
    # await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)