from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.default.main_buttons import main_menu_buttons
from loader import dp, _


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = (_("Список команд: ",
              "/start - Начать диалог",
              "/help - Получить справку",
              "/restart - Если что-то пойдет не так"))

    await message.answer("\n".join(text))


@dp.message_handler(Command(['restart']), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(_('упсс все норм ?'),
                         reply_markup=main_menu_buttons)
