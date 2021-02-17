from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


# def answer_kb(answers, question_id):
#     answer_buttons = [InlineKeyboardButton(text=answer, callback_data=(answer + ';' + str(question_id))) for answer in
#                       answers]
#
#     kb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
#         answer_buttons
#     ],
#     )
#
#     return kb


def answer_kb(answers, question_id):
    nums = list(answers.keys())
    random.shuffle(nums)
    keyboard = InlineKeyboardMarkup()
    [keyboard.add(
        InlineKeyboardButton(
            text=answers[num],
            callback_data=f"{num};{question_id}"
        )
    )
        for num in nums]
    return keyboard


add_to_db = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='add to db', callback_data='add_db'),
            InlineKeyboardButton(text="Cancel❌", callback_data='cancel')
        ]
    ],
    resize_keyboard=True
)

languages_markup = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Русский🇷🇺", callback_data="lang_ru")],
        [
            InlineKeyboardButton(text="Uzbek🇺🇿", callback_data="lang_uz"),
        ]
    ]
)

languages_markup2 = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Русский🇷🇺", callback_data="lang2_ru")],
        [
            InlineKeyboardButton(text="Uzbek🇺🇿", callback_data="lang2_uz"),
        ]
    ]
)
