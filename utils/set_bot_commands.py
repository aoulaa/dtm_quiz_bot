from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("add_question", "толко для админов"),
        types.BotCommand("add_con", "толко для админов"),
        types.BotCommand("/restart",  "Если что-то пойдет не так")
    ])
