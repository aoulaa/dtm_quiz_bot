from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino
from aiogram import executor
from utils.notify_admins import on_startup_notify
from handlers import dp


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await set_default_commands(dispatcher)
    await db_gino.on_startup(dispatcher)
    # await db.gino.drop_all()
    await db.gino.create_all()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
