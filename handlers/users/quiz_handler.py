import json
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.dict_pack import dict_of_topics
from keyboards.default.main_buttons import rating_buttons
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
    random.shuffle(answers)  # Мешаем ответы для исключения возможности ответа по зрительной памяти
    text_1 = 'Choose the correct answer'
    text_2 = questions_by_topic[0].explanation
    if text_2 is not None:
        text = f'{text_2}.\n\n{questions_by_topic[0].questions}'
    else:
        text = f'{text_1}.\n\n{questions_by_topic[0].questions}'
    await message.answer(text=text, reply_markup=answer_kb(answers, questions_by_topic[0].id))
    # В последнюю очередь отправляем сам вопрос с кнопками. По-хорошему надо бы записывать номер этого сообщения
    # для последующего удаления, оставлю это тебе, это необязательно.


@dp.callback_query_handler(state=Data.present_data)
async def get_answer(call: CallbackQuery, state: FSMContext):
    # id_u = call.message.from_user.id
    # if id_u != id_u:
    #     await call.message.answer('sorry bro')
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
    random.shuffle(answers)  # Мешаем ответы для исключения возможности ответа по зрительной памяти

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
    question = None
    usr = await commands.select_user(id_user)
    stats = json.loads(usr.stats)
    rating = usr.rating
    for key, value in answered.items():
        question = await commands.select_questions(int(key))
        count += 1
        text += f'{question.questions} ❌ ({question.right_answer})\n\n' \
            if question.right_answer != value \
            else f'{question.questions} ✔️\n\n'
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


async def get_best_questions(id_user, topic, num=5):
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


@dp.message_handler(text='📊 Рейтинг')
async def get_to_ratings(msg: types.Message):
    text = """Это рейтинг игроков. 

Выполняй задания каждый день и получай рейтинговые очки!

Чтобы перейти в лигу выше нужно набрать минимум очков для перехода и войти в топ 3 игроков лиги.

Минимумы очков:
🥉 ->🥈 500
🥈 ->🥇 1000
🥇 ->💎 1900

Здесь ты можешь увидеть на каком ты месте и в какой лиге сейчас:"""
    await msg.answer(text, reply_markup=rating_buttons)


@dp.message_handler(text='🕴 Мой рейтинг')
async def get_my_rating(msg: types.Message):
    id = msg.from_user.id
    users = await commands.select_all_users()
    text = await my_rating(users, id)
    await msg.answer(text)


@dp.message_handler(text='🌎 Топ 10')
async def get_all_rating(msg: types.Message):
    users = await commands.select_all_users()
    text = await all_ratings(users)
    await msg.answer(text)


# counting ratings
async def my_rating(users, user_id):
    text = ''
    for num, usr in enumerate(users, 1):
        if usr.id == user_id:
            text += f'{num}) {usr.name} {usr.rating}💎\n'
    return text


async def all_ratings(users):
    text = ''

    for num, usr in enumerate(users, 1):
        text += f'{num}) {usr.name} {usr.rating}💎\n'
        if num == 7:  # 10 из топа
            return text
