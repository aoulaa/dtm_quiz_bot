from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_b = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Present simple')],
        [KeyboardButton(text='Past simple')]

              ],
    resize_keyboard=True

)