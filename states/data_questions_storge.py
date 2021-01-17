from aiogram.dispatcher.filters.state import StatesGroup, State


class Data(StatesGroup):

    present_data = State()


class Admin(StatesGroup):
    add_topic = State()
    add_question = State()
    add_right_answer = State()
    add_wrong_answer = State()
    question_dis = State()

