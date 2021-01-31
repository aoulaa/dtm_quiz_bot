from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino, commands
from aiogram import executor
from utils.notify_admins import on_startup_notify
from handlers import dp


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await set_default_commands(dispatcher)
    await db_gino.on_startup(dispatcher)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_question("present_simple", "i ... from Russia", 'am', 'is,are,has', 'you got what you need')
    await commands.add_question("present_simple", "you ... my friend", 'are', 'is,am,have', 'yes man got what you need')
    await commands.add_question("present_simple", "He ... my son", 'is', 'nor,are,has')
    await commands.add_question("present_simple", "they ... working with me", 'are', 'is,am,have')
    await commands.add_question("present_simple", "IT ... very good place to work and grow", 'is', 'are,am,have')
    await commands.add_question("present_simple", "They ... selling things ", 'are', 'is,am,have')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
