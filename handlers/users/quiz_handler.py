import json
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.dict_pack import dict_of_topics

from keyboards.inline.in_buttons import answer_kb
from loader import dp

from states import Data
from utils.db_api import commands
from collections import OrderedDict
from operator import itemgetter


@dp.message_handler(text=dict_of_topics, state="*")
async def send_present_q(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    await state.update_data(id=id_user)
    questions_by_topic = await get_best_questions(id_user, dict_of_topics[message.text])
    await state.update_data(questions_all=questions_by_topic)  # А тут обновляем данные в FSM
    await state.update_data(answered={})  # Здесь создадим пустой словарь, в который позже запишем ответы
    await Data.present_data.set()
    random.shuffle(questions_by_topic)  # Мешаем вопросы, чтобы выдать случайный вопрос из списка
    answers = questions_by_topic[0].wrong_answer.split(',')
    # Получаем здесь ответы на вопросы, чтобы передать их в клавиатуре
    answers.append(questions_by_topic[0].right_answer)
    last_q_dict = {}
    for num, ans in enumerate(answers):  # Готовим словарь с ответами - нужно для обхода ограничений cb_data
        last_q_dict[num] = ans
    await state.update_data(last_question_dict=last_q_dict)
    text = await explanation_text(questions_by_topic)
    await message.answer(text=text, reply_markup=answer_kb(last_q_dict, questions_by_topic[0].id))
    # В последнюю очередь отправляем сам вопрос с кнопками. По-хорошему надо бы записывать номер этого сообщения
    # для последующего удаления, оставлю это тебе, это необязательно.


@dp.callback_query_handler(state=Data.present_data)
async def get_answer(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    answer, q_id = call.data.split(';')  # тут получаем коллбек дату и сразу распаковываем ее в ID и ответ.
    data = await state.get_data()  # Получаем данные из FSM
    id_user = data.get('id')
    answered = data.get('answered')
    all_question = data.get('questions_all')
    previous_question_dict = data.get('last_question_dict')
    answer = previous_question_dict[int(answer)]
    answered[q_id] = answer  # Записываем в словарь ответ на вопрос.
    if len(answered.keys()) == 4:  # Проерка числа отвеченных вопросов. Если больше этого числа - закончим квиз.
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
    last_q_dict = {}
    for num, ans in enumerate(answers):  # Готовим словарь с ответами - нужно для обхода ограничений cb_data
        last_q_dict[num] = ans
    await state.update_data(last_question_dict=last_q_dict)
    text = await explanation_text(all_question)
    await call.message.answer(text=text, reply_markup=answer_kb(last_q_dict, all_question[0].id))
    # В конце посылаем новый вопрос.


async def make_summary(id_user, answered):  # функция подсчет статистики.
    text = ''
    score = 0
    count = 0
    question = None
    usr = await commands.select_user(id_user)
    stats = json.loads(usr.stats)
    rating = usr.rating
    for num, (key, value) in enumerate(answered.items(), 1):
        question = await commands.select_questions(int(key))
        count += 1
        text += f'{num}. {question.questions} ❌ ({question.right_answer})\n\n' \
            if question.right_answer != value \
            else f'{num}. {question.questions} ✅ ({question.right_answer}) \n\n'
        if question.right_answer == value:
            rating += 1
            score += 1
            if not stats.get(key):
                stats[key] = 0
            stats[key] += 1
    await commands.update_user_stats(id_user, json.dumps(stats))
    await commands.update_rating(id_user, rating)
    text += f"<b>Out of {count}/{str(score)}</b>"
    ready_text = f'<b>Theme:</b> {question.topic}\n\n{text}'
    return ready_text


async def get_best_questions(id_user, topic, num=20):
    questions = await commands.select_question_by_topic(topic)
    questions_ids = [q.id for q in questions]  # Генерируем список ID вопросов для дальнейшей обработки.
    usr = await commands.select_user(id_user)
    stats = json.loads(usr.stats)  # Получаем статистику и конвертируем(десериализуем) ее в словарь.

    for q in questions_ids:  # Заполняем статистику нулями для непредставленных в статистике вопросов.
        if not stats.get(str(q)):
            stats[str(q)] = 0
    stats = OrderedDict(sorted(stats.items(), key=itemgetter(1)))  # Сортируем словарь по значению - количеству раз,
    # которые вопрос был задан
    best_questions_ids = []  # Здесь и далее из сортированного словаря получаем список вопросов
    for key, _ in stats.items():
        best_questions_ids.append(key)
    best_questions_ids = best_questions_ids[0:num]  # Это число ограничивает список вопросов для квиза
    best_questions = [best_q for best_q in questions
                      if str(best_q.id) in best_questions_ids]  # Немного магии от
    # генератора списка. Тут получаем объекты вопросов, которые встречались реже всего.
    return best_questions


async def explanation_text(quetions_explanation):
    text_1 = 'Choose the correct answer'
    text_2 = quetions_explanation[0].explanation
    if text_2 is not None:
        text = f'<b>{text_2}</b>\n\n{quetions_explanation[0].questions}'
    else:
        text = f'<b>{text_1}</b>\n\n{quetions_explanation[0].questions}'
    return text
