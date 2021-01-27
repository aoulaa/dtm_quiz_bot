from aiogram.types import CallbackQuery

from keyboards.default.main_buttons import main_menu_buttons
from loader import dp, _
from utils.db_api import commands


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    id = call.from_user.id

    lang = call.data[-2:]
    await commands.update_language(id, lang)

    await call.message.answer(_("Ваш язык был изменен", locale=lang),
                              reply_markup=main_menu_buttons)
