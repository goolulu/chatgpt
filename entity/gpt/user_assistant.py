from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

from datasource.dataSourceConfig import session

Base = declarative_base()


class UserAssistant(Base):
    __tablename__ = 'user_assistant'

    user_id = Column(Integer, primary_key=True)
    assistant_id = Column(String(64))
    thread_id = Column(String(64))


def get_user_assistant() -> UserAssistant:
    return session.query(UserAssistant).all()
