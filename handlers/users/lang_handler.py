import typing
from dataclasses import dataclass

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.in_buttons import languages_markup, languages_markup2
from loader import dp, _
from utils.db_api import commands


@dataclass
class ListOfButtons:
    text: typing.List
    callback: typing.List = None
    align: typing.List[int] = None
    """
    Использование:
    ListOfButtons(text=["Кнопка", "Кнопка", "Кнопка", "Кнопка"],
                  callback=["callback1", "callback2", "callback3", "callback4"],
                  align=[1, 2, 1]).keyboard
    row_sizes - количество кнопок в ряде
    """

    @property
    def inline_keyboard(self):
        return generate_inline_keyboard(self)

    @property
    def reply_keyboard(self):
        return generate_reply_keyboard(self)


def generate_inline_keyboard(args: ListOfButtons) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    if args.text and args.callback and not (len(args.text) == len(args.callback)):
        raise IndexError("Все списки должны быть одной длины!")

    if not args.align:
        for num, button in enumerate(args.text):
            keyboard.add(InlineKeyboardButton(text=str(button),
                                              callback_data=str(args.callback[num])))
    else:
        count = 0
        for row_size in args.align:
            keyboard.row(*[InlineKeyboardButton(text=str(text), callback_data=str(callback_data))
                           for text, callback_data in
                           tuple(zip(args.text, args.callback))[count:count + row_size]])
            count += row_size
    return keyboard


def generate_reply_keyboard(args: ListOfButtons) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    if not args.align:
        for num, button in enumerate(args.text):
            keyboard.add(KeyboardButton(text=str(button)))
    else:
        count = 0
        for row_size in args.align:
            keyboard.row(*[KeyboardButton(text=str(text)) for text in args.text[count:count + row_size]])
            count += row_size
    return keyboard


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    id = call.message.chat.id
    lang = call.data[-2:]
    await commands.update_language(id, lang)
    menu = ListOfButtons(
        text=[_("🧠 Заниматься", locale=lang),
              _("📊 Рейтинг", locale=lang),
              _("язык🔁", locale=lang)
              ],
        align=[1, 2]
    ).reply_keyboard
    if '2' not in call.data:
        text = _('Добро пожаловать, надеюсь тебе тут понравится.', locale=lang)
    else:
        text = _("Ваш язык был изменен, вы находитесь в главном меню", locale=lang)

    await call.message.answer(text,
                              reply_markup=menu)


@dp.message_handler(text=_('язык🔁'), state="*")
async def bot_language(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(_('Хотите изменить язык?'),
                         reply_markup=languages_markup2)
