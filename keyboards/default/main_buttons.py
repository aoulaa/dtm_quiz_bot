from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="тесты по теме")],
        [KeyboardButton(text="Рейтинг")]
    ],
    resize_keyboard=True
)

topic_for_admins = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='bаck')],
        [KeyboardButton(text='present_simple')],
        [KeyboardButton(text='past_simple')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Add new questions")]
    ],
    resize_keyboard=True
)


test_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="назад")],
        [KeyboardButton(text='Present simple')],
        [KeyboardButton(text='Past simple')]

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
