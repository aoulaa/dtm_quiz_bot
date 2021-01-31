from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота/Botni ishga tushirish"),
        types.BotCommand("help", "Помощь/Yordam"),
        types.BotCommand("restart", "Если что-то пойдет не так/Agar biror xatolig bo'lsa"),
        types.BotCommand("add_question", "только для админов"),
        types.BotCommand("add_con", "только для админов"),

    ])
