from aiogram import Dispatcher


from loader import dp
from .throttling import ThrottlingMiddleware
from .language_middleware import ACLMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
