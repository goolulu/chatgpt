import os

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

from datasource.dataSourceConfig import Session

Base = declarative_base()


class UserAssistant(Base):
    __tablename__ = 'user_assistant'

    user_id = Column(Integer, primary_key=True)
    assistant_id = Column(String(64))
    thread_id = Column(String(64))


def get_user_assistant() -> UserAssistant:
    return Session().query(UserAssistant).filter_by(user_id=os.environ.get("user_id")).first()


def update_user_assistant(assistant_id):
    session = Session()
    session.query(UserAssistant).filter_by(user_id=1).update({'assistant_id': assistant_id})
    session.commit()


def create_user_assistant(user_assistant: UserAssistant):
    session = Session()
    ua = session.query(UserAssistant).filter_by(user_id=user_assistant.user_id).first()
    if ua:
        raise "该用户已经添加助手"
    session.add(user_assistant)
    session.commit()
