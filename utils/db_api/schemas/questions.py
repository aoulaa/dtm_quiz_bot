from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger)
    name = Column(String(100))
    number_times = Column(String(20000))

    referral = Column(BigInteger)

    query: sql.Select


class Questions(TimedBaseModel):
    __tablename__ = 'tests'
    id = Column(BigInteger, primary_key=True)
    topic = Column(String(500))
    questions = Column(String(2000))
    right_answer = Column(String(100))
    wrong_answer = Column(String(1000))
    explanation = Column(String(1500))

    referral = Column(BigInteger)

    query: sql.Select