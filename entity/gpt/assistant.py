from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import update

from datasource.dataSourceConfig import session

Base = declarative_base()


class Assistant(Base):
    __tablename__ = 'assistant'
    id = Column(String(64), primary_key=True)
    name = Column(String(100))
    instructions = Column(String(2000))
    model = Column(String(32))

    def __init__(self, id, name, instructions, model):
        self.id = id
        self.name = name
        self.instructions = instructions
        self.model = model


def get_assistant() -> Assistant:
    return session.query(Assistant).all()


def update_assistant(assistant):
    update(Assistant).where()
