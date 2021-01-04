import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.in_buttons import answer_kb
from loader import dp

from states import Data
from utils.db_api import commands

dict_of_topics = {
    'Present simple': 'present_simple',
    'Past simple': 'past_simple'
}


@dp.message_handler(text=dict_of_topics)
async def send_present_q(message: types.Message, state: FSMContext):
    question_p = await commands.select_question_by_topic(
        dict_of_topics[message.text])  # Здесь получаем список вопросов по теме
    await state.update_data(questions_all=question_p)  # А тут обновляет данные в FSM
    await state.update_data(answered={})  # Здесь создадим пустой словарь, в который позже запишем ответы
    # await message.answer('Present simple', reply_markup=present_buttons)  # передаю инлайн кнопки
    await Data.present_data.set()
    """add func here"""
    """also get user id"""
    random.shuffle(question_p)  # Мешаем вопросы, чтобы выдать случайный вопрос из списка
    answers = question_p[0].wrong_answer.split(',')  # Получаем здесь ответы на вопросы, чтобы передать их в клавиатуре
    answers.append(question_p[0].right_answer)
    random.shuffle(answers)  # Мешаем ответы для исключения возможности ответа по зрительной памяти
    text = f'Choose the correct answer.\n\n{question_p[0].questions}'
    await message.answer(text=text, reply_markup=answer_kb(answers, question_p[0].id))
    # В последнюю очередь отправляем сам вопрос с кнопками. По-хорошему надо бы записывать номер этого сообщения
    # для последующего удаления, оставлю это тебе, это необязательно.


@dp.callback_query_handler(state=Data.present_data)
async def get_answer(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()  # Тут удаляем инлайн клавиатуру (хм...)
    await call.message.delete()
    answer, q_id = call.data.split(';')  # тут получаем коллбек дату и сразу распаковываем ее в ID и ответ.
    data = await state.get_data()  # Получаем данные из FSM
    answered = data.get('answered')
    q_p = data.get('questions_all')
    answered[q_id] = answer  # Записываем в словарь ответ на вопрос.
    if len(answered.keys()) == 5:  # Проерка числа отвеченных вопросов. Если больше этого числа - закончим квиз.
        summary = await make_summary(answered)  # Считаем статистику. Функция корявая,
        await state.reset_state(with_data=False)  # но опять же, оставлю тебе на разбор и допил.
        await call.message.answer(summary)
        return
    while answered.get(str(q_p[0].id)):  # Тут рандомизируем список так, чтобы обращение к списку вопросов по [0]
        random.shuffle(q_p)  # возвращало вопрос, который еще не был задан пользователю.
    await state.update_data(questions_all=q_p)
    await state.update_data(answered=answered)
    answers = q_p[0].wrong_answer.split(',')
    answers.append(q_p[0].right_answer)
    text = f'Choose the correct answer.\n\n{q_p[0].questions}'
    await call.message.answer(text=text, reply_markup=answer_kb(answers, q_p[0].id))
    # В конце посылаем новый вопрос.


async def make_summary(answered):  # функция подсчет статистики.
    global question, value
    text = ''
    score = 0
    for key, value in answered.items():
        question = await commands.select_questions(int(key))
        text += f'{question.questions} ❌ ({question.right_answer})\n\n' \
            if question.right_answer != value else f'{question.questions} ✔️\n\n'
        print(key)
        if question.right_answer == value:
            score += 1
        if question.right_answer == value:
            await commands.add_user_with_id(int(key))

    text += f"<b>Out of 30/{str(score)}</b>"
    ready_text = f'<b>Theme:</b> {question.topic}\n\n{text}'

    return ready_text

# # пока пуст так останется позже перепишу нормално
# @dp.callback_query_handler(text='present_simple_cb', state=Data.present_data)
# async def get_questions(call: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     questions = data.get("questions_present")
#     await call.message.answer(f'вопроси {questions}')  # не вся функция просто провераю работает ли
#     print(questions)
#
#     await call.message.delete_reply_markup()
