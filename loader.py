from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

from utils.db_api.db_gino import db

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

from middlewares.language_middleware import setup_middleware

__all__ = ["bot", "storage", "dp", "db", "_"]

i18n = setup_middleware(dp)

_ = i18n.lazy_gettext
