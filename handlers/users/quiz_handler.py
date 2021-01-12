import json
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
    id_user = message.from_user.id
    await state.update_data(id=id_user)
    select_ques_by_topic = await commands.select_question_by_topic(
        dict_of_topics[message.text])  # Здесь получаем список вопросов по теме
    await state.update_data(questions_all=select_ques_by_topic)  # А тут обновляет данные в FSM
    await state.update_data(answered={})  # Здесь создадим пустой словарь, в который позже запишем ответы
    await Data.present_data.set()

    random.shuffle(select_ques_by_topic)  # Мешаем вопросы, чтобы выдать случайный вопрос из списка
    answers = select_ques_by_topic[0].wrong_answer.split(
        ',')  # Получаем здесь ответы на вопросы, чтобы передать их в клавиатуре
    answers.append(select_ques_by_topic[0].right_answer)
    random.shuffle(answers)  # Мешаем ответы для исключения возможности ответа по зрительной памяти
    text_1 = 'Choose the correct answer'
    text_2 = select_ques_by_topic[0].explanation
    if text_2 is not None:
        text = f'{text_2}.\n\n{select_ques_by_topic[0].questions}'
    else:
        text = f'{text_1}.\n\n{select_ques_by_topic[0].questions}'
    await message.answer(text=text, reply_markup=answer_kb(answers, select_ques_by_topic[0].id))
    # В последнюю очередь отправляем сам вопрос с кнопками. По-хорошему надо бы записывать номер этого сообщения
    # для последующего удаления, оставлю это тебе, это необязательно.


@dp.callback_query_handler(state=Data.present_data)
async def get_answer(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()  # Тут удаляем инлайн клавиатуру (хм...)
    await call.message.delete()
    answer, q_id = call.data.split(';')  # тут получаем коллбек дату и сразу распаковываем ее в ID и ответ.
    data = await state.get_data()  # Получаем данные из FSM
    id_user = data.get('id')
    answered = data.get('answered')
    all_question = data.get('questions_all')
    answered[q_id] = answer  # Записываем в словарь ответ на вопрос.

    if len(answered.keys()) == 5:  # Проерка числа отвеченных вопросов. Если больше этого числа - закончим квиз.
        summary = await make_summary(id_user, answered)
        await state.reset_state(with_data=False)
        await call.message.answer(summary)
        return

    while answered.get(
            str(all_question[0].id)):  # Тут рандомизируем список так, чтобы обращение к списку вопросов по [0]
        random.shuffle(all_question)  # возвращало вопрос, который еще не был задан пользователю.
    await state.update_data(questions_all=all_question)
    await state.update_data(answered=answered)
    answers = all_question[0].wrong_answer.split(',')
    answers.append(all_question[0].right_answer)

    text_1 = 'Choose the correct answer'
    text_2 = all_question[0].explanation
    if text_2 is not None:
        text = f'{text_2}.\n\n{all_question[0].questions}'
    else:
        text = f'{text_1}.\n\n{all_question[0].questions}'
    await call.message.answer(text=text, reply_markup=answer_kb(answers, all_question[0].id))
    # В конце посылаем новый вопрос.


async def make_summary(id_user, answered):  # функция подсчет статистики.
    text = ''
    score = 0
    count = 0
    con = 0
    question = None
    dict_num = {}
    print(dict_num)
    await commands.add_user_with_id(id_user, json.dumps(dict_num))
    # await commands.update_ques(id_user, json.dumps(dict_num))
    for key, value in answered.items():
        con += 1
        dict_num[key] = con
        question = await commands.select_questions(int(key))
        count += 1
        text += f'{question.questions} ❌ ({question.right_answer})\n\n' \
            if question.right_answer != value \
            else f'{question.questions} ✔️\n\n'
        if question.right_answer == value:
            score += 1

    text += f"<b>Out of {count}/{str(score)}</b>"
    ready_text = f'<b>Theme:</b> {question.topic}\n\n{text}'
    return ready_text
