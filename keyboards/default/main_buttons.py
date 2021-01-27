from loader import _
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("🧠 Заниматься"))],
        [KeyboardButton(text=_("📊 Рейтинг"))]
    ],
    resize_keyboard=True
)


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Add new questions")]
    ],
    resize_keyboard=True
)

description = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Choose the correct answer")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

con_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='add con')],
        [KeyboardButton(text='remove con')],
    ],
    resize_keyboard=True,
)

rating_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("🌎 Топ 10")), KeyboardButton(text=_("🕴 Мой рейтинг"))],
        [KeyboardButton(text=_("назад"))]
    ],
    resize_keyboard=True,
)


def genrate_button(buttons, key):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=key)
    keyboard.add(*buttons)
    return keyboard


