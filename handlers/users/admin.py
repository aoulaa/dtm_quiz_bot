from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.dict_pack import list_of_topics, topic_for_admins
from keyboards.default.main_buttons import admin_button, description, con_buttons, genrate_button
from keyboards.inline.in_buttons import add_to_db

from states import Admin
from utils.db_api import commands

from aiogram import types
from filters import IsPrivate
from loader import dp

from data.config import contributor, admins


# @dp.message_handler(text="backk", state="*")
# async def go_back(msg: types.Message, state: FSMContext):
#     text = ''
#     state_name = await state.get_state()
#     if state_name is not None:
#         await Admin.previous()
#         if state_name == Admin.add_question:
#             text = 'Send the question in this format:\n<b>I .... doctor.</b>'
#
#     await msg.answer(text)


@dp.message_handler(IsPrivate(), commands='add_question')
async def add_question(msg: types.Message):
    id = msg.from_user.id

    if id not in contributor:
        await msg.answer(f'You are not admin 🧐\nInvalid ID: {id}')
    else:
        await msg.answer("Welcome dear contributor🤗\n\nWhat would you like to do today ?",
                         reply_markup=admin_button)


@dp.message_handler(user_id=contributor, text='Add new questions', state="*")
async def chose_topic(msg: types):
    await msg.answer('Choose the topic you want to add questions to',
                     reply_markup=genrate_button(topic_for_admins, True))
    await Admin.add_topic.set()


@dp.message_handler(state=Admin.add_topic)
async def save_topic(msg: types, state: FSMContext):
    topic_name = msg.text
    if topic_name not in list_of_topics:
        await msg.answer('Please send exciting topic or choose from buttons below.❗')
    else:
        await state.update_data(topic_name=topic_name)
        await msg.answer('Send the question in this format:\n<b>I .... doctor.</b>')
        await Admin.add_question.set()


@dp.message_handler(state=Admin.add_question)
async def save_question(msg: types, state: FSMContext):
    question = msg.text
    await state.update_data(question=question)
    await msg.answer('Send the right answer to the question')
    await Admin.add_right_answer.set()


@dp.message_handler(state=Admin.add_right_answer)
async def save_right_answer(msg: types, state: FSMContext):
    right_answer = msg.text
    await state.update_data(right_answer=right_answer)
    await msg.answer('Send the wrong answers in this format: \n\n am,are,is')
    await Admin.add_wrong_answer.set()


@dp.message_handler(state=Admin.add_wrong_answer)
async def save_question_dis(msg: types, state: FSMContext):
    wrong_answer = msg.text
    await state.update_data(wrong_answer=wrong_answer)
    await msg.answer('Send task description or choose below',
                     reply_markup=description)
    await Admin.question_dis.set()


@dp.message_handler(state=Admin.question_dis)
async def save_send_db(msg: types, state: FSMContext):
    description = msg.text
    await state.update_data(description=description)
    data = await state.get_data()
    topic_name = data.get("topic_name")
    question = data.get("question")
    right_answer = data.get("right_answer")
    wrong_answer = data.get("wrong_answer")

    text = f'<b>Question is being add to this topic:</b>\n"{topic_name}"\n\n' \
           f'<b>Question itself:</b>\n"{question}"\n\n' \
           f'<b>Right answer:</b>\n"{right_answer}"\n\n' \
           f'<b>Wrong answer:</b>\n"{wrong_answer}"\n\n' \
           f'<b>description of the question:</b>\n"{description}"'
    await msg.answer(text, reply_markup=add_to_db)
    await Admin.ready_to_add.set()


@dp.callback_query_handler(state=Admin.ready_to_add, text=['add_db', 'cancel'])
async def confirm(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["back", data['topic_name']]
    keyboard.add(*buttons)
    if call.data == 'add_db':
        await commands.add_question(data['topic_name'], data['question'],
                                    data['right_answer'], data['wrong_answer'],
                                    data['description'])

        await call.message.delete()
        await call.message.answer('Question is added✅', reply_markup=keyboard)
        await Admin.add_topic.set()

    elif call.data == 'cancel':
        await call.message.delete()
        await call.message.answer('Question is cancelled', reply_markup=keyboard)
        await Admin.add_topic.set()


# for admin only to add new contributors
@dp.message_handler(IsPrivate(), commands='add_con')
async def add_question(msg: types.Message):
    if msg.from_user.id not in admins:
        await msg.answer('You are not admin 🧐')
    else:
        await msg.answer("Welcome back 🤗\n\nWhat would you like to do ?",
                         reply_markup=con_buttons)


# adding to the list of contributors
@dp.message_handler(user_id=admins, text='add con')
async def add_con(msg: types.Message, state: FSMContext):
    await msg.answer('Send contributor ID.\nFor example: 10548615489')
    await state.set_state('add_con')


@dp.message_handler(state='add_con')
async def adding_con(msg: types.Message, state: FSMContext):

    if not msg.text.isdigit():
        await msg.answer('Please send contributor\'s ID which should be digit')
    else:
        contributor.append(msg.text)
        await msg.answer(f'<b>{msg.text}</b> is added to the list of contributors\n\n{contributor}')
        await state.finish()


# removing from the list of contributors
@dp.message_handler(user_id=admins, text='remove con')
async def remove_con(msg: types.Message, state: FSMContext):
    await msg.answer(f'To remove from contributors send contributor ID.\nFor example: 10548615489'
                     f'\n\nlist of contributors: {contributor}')
    await state.set_state('remove_con')


@dp.message_handler(state='remove_con')
async def removing_con(msg: types.Message, state: FSMContext):

    if not msg.text.isdigit():
        await msg.answer('Please send contributor\'s ID which should be digit')
    elif msg.text in contributor:
        contributor.remove(msg.text)
        await msg.answer(f'<b>{msg.text}</b> is removed from the list of contributors\n\n{contributor}')
        await state.finish()
    else:
        await msg.answer('Please choose ID from the list above, you would like to delete')
