from sqlalchemy import Column, String, insert, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import update

from datasource.dataSourceConfig import session

Base = declarative_base()


class Assistant(Base):
    __tablename__ = 'assistant'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    instructions = Column(String(2000))
    model = Column(String(32))

    def __init__(self, id, name, instructions, model, assistant_id):
        self.id = id
        self.name = name
        self.instructions = instructions
        self.model = model
        self.assistant_id = assistant_id


def get_assistant() -> Assistant:
    return session.query(Assistant).all()

