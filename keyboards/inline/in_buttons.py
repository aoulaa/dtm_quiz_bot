from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def answer_kb(answers, question_id):
    answer_buttons = [InlineKeyboardButton(text=answer, callback_data=(answer + ';' + str(question_id))) for answer in
                      answers]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        answer_buttons
    ]
    )
    return kb


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
