from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def answer_kb(answers, question_id):
    answer_buttons = [InlineKeyboardButton(text=answer, callback_data=(answer + ';' + str(question_id))) for answer in
                      answers]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        answer_buttons
    ]
    )
    return kb
