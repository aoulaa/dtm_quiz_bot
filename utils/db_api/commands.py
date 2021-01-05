from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.questions import Questions, User


async def add_user_with_id(questions_ids: int):
    try:
        user = User( questions_ids=questions_ids)
        await user.create()

    except UniqueViolationError:
        pass


async def add_user_id(id: int):
    try:
        user = User(id=id)
        await user.create()

    except UniqueViolationError:
        pass


async def add_question(topic: str, questions: str, right_answer: str, wrong_answer: str):
    try:
        question = Questions(topic=topic, questions=questions,
                             right_answer=right_answer, wrong_answer=wrong_answer)
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
