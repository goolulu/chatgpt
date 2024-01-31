from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datasource.dataSourceConfig import Session

Base = declarative_base()


class FunctionInfo(Base):
    __tablename__ = 'function_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(1024))

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


def get_all_function():
    return Session().query(FunctionInfo).all()

