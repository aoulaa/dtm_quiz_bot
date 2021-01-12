from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.questions import Questions, User


async def add_user_with_id(id: int, number_times: str):
    try:
        user = User(id=id, number_times=number_times)
        await user.create()

    except UniqueViolationError:
        pass


async def select_quest_id_by_user_id(use_id):
    user = await User.query.where(User.id == use_id).gino.all()
    return user


async def add_question(topic: str, questions: str, right_answer: str, wrong_answer: str, explanation: str = None):
    try:
        question = Questions(topic=topic, questions=questions,
                             right_answer=right_answer, wrong_answer=wrong_answer,
                             explanation=explanation)
        await question.create()

    except UniqueViolationError:
        pass


async def select_question_by_topic(topics):
    questions = await Questions.query.where(Questions.topic == topics).gino.all()
    return questions


async def select_all_question():
    question = await Questions.query.gino.all()
    return question


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def select_questions_id(questions_ids: int):
    user = await User.query.where(User.questions_ids == questions_ids).gino.all()
    return user


async def select_questions(id: int):
    questions = await Questions.query.where(Questions.id == id).gino.first()
    return questions


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def count_questions():
    total = await db.func.count(Questions.id).gino.scalar()
    return total


async def update_ques(id, number_times: str):
    user = await User.get(id)
    await user.update(number_times=number_times).apply()
