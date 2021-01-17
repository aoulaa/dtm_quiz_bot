from aiogram.dispatcher import FSMContext

from data.dict_pack import list_of_topics
from keyboards.default.main_buttons import admin_button, topic_for_admins, description
from loader import dp
from aiogram import types

from states import Admin
from utils.db_api import commands


@dp.message_handler(commands='add_question')
async def add_question(msg: types.Message):
    await msg.answer("Let's start adding questions",
                     reply_markup=admin_button)


@dp.message_handler(text='Choose a topic', state="*")
async def chose_topic(msg: types):
    await msg.answer('choose the topic you want to add questions to',
                     reply_markup=topic_for_admins)
    await Admin.add_topic.set()


@dp.message_handler(state=Admin.add_topic)
async def save_topic(msg: types, state: FSMContext):
    topic_name = msg.text
    if topic_name not in list_of_topics:
        await msg.answer('please send exciting topic')
    else:
        await state.update_data(topic_name=topic_name)
        await msg.answer('Send the question in this format:\n I .... doctor.')
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
    data = await state.get_data()
    topic_name = data.get("topic_name")
    question = data.get("question")
    right_answer = data.get("right_answer")
    wrong_answer = data.get("wrong_answer")
    descr = msg.text
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["back", topic_name]
    keyboard.add(*buttons)
    await commands.add_question(topic_name, question, right_answer, wrong_answer, descr)
    await msg.answer('question is added', reply_markup=keyboard)
    await state.finish()
    await Admin.add_topic.set()

