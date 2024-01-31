from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datasource.dataSourceConfig import Session

Base = declarative_base()


class FunctionParameters(Base):
    __tablename__ = 'function_parameters'

    id = Column(Integer, primary_key=True)
    function_id = Column(Integer)
    function_name = Column(String)
    name = Column(String)
    type = Column(String)
    enum = Column(String)
    description = Column(String)
    required = Column(Boolean)

    def __init__(self, function_id, function_name, name,
                 type, enum, description, required
                 ):
        self.function_id = function_id
        self.function_name = function_name
        self.name = name
        self.type = type
        self.enum = enum
        self.description = description
        self.required = required


def get_all_function_param():
    return Session().query(FunctionParameters).all()

