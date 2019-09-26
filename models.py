from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, create_engine

Base = declarative_base()


class Results(Base):
    __tablename__ = 'calculator_results'

    id = Column(Integer, primary_key=True)
    first_number = Column('First number', String)
    action = Column('Action', String)
    second_number = Column('Second number', String)
    result = Column('Results', String)

    def __init__(self, first_number, action, second_number, result):
        self.first_number = first_number
        self.action = action
        self.second_number = second_number
        self.result = result
