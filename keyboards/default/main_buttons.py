from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧠 Заниматься")],
        [KeyboardButton(text="📊 Рейтинг")]
    ],
    resize_keyboard=True
)

# topic_for_admins = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='bаck')],
#         [KeyboardButton(text='present_simple')],
#         [KeyboardButton(text='past_simple')]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True
# )

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
        [KeyboardButton(text="🌎 Топ 10"), KeyboardButton(text="🕴 Мой рейтинг")],
        [KeyboardButton(text="назад")]
    ],
    resize_keyboard=True
)


def genrate_button(buttons):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*buttons)
    return keyboard

