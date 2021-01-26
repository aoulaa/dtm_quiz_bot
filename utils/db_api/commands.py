from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.questions import Questions, User


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
    users = await User.query.order_by(User.rating.desc()).gino.all()
    return users


async def add_user(user_id: int, name: str, stats: str, rating: int, referral: int = 1079453114):
    try:
        user = User(id=user_id, name=name, stats=stats, rating=rating, referral=referral)
        await user.create()

    except UniqueViolationError:
        pass


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


async def update_rating(id: int, rating: int):
    user = await User.query.where(User.id == id).gino.first()
    await user.update(rating=rating).apply()


async def update_user_stats(id: int, stats: str):
    user = await User.query.where(User.id == id).gino.first()
    await user.update(stats=stats).apply()


async def update_language(id: int, language: str):
    user = await User.query.where(User.id == id).gino.first()
    await user.update(language=language).apply()
