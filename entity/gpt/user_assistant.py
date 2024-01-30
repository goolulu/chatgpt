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


def update_user_assistant(assistant_id):
    session.query(UserAssistant).filter_by(user_id=1).update({'assistant_id': assistant_id})
    session.commit()