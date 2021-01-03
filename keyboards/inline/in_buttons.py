from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

present_buttons = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Test 1", callback_data='present_simple_cb'),
            InlineKeyboardButton(text="Test 2", callback_data='test2_cb')
        ],
        [
            InlineKeyboardButton(text="Test 3", callback_data='test3_cb'),
            InlineKeyboardButton(text="Test 4", callback_data='test4_cb')
        ],
        [
            InlineKeyboardButton(text="Test 5", callback_data='test5_cb'),
            InlineKeyboardButton(text="Test 6", callback_data='test6_cb')
        ],

    ], resize_keyboard=True)


def answer_kb(answers, question_id):
    answer_buttons = [InlineKeyboardButton(text=answer, callback_data=(answer + ';' + str(question_id))) for answer in
                      answers]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        answer_buttons
    ]
    )
    return kb
