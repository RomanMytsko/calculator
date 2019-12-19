from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, create_engine, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Results(Base):
    __tablename__ = 'calculator_results'

    id = Column(Integer, primary_key=True)
    first_number = Column('First number', String)
    action = Column('Action', String)
    second_number = Column('Second number', String)
    result = Column('Results', String)
    user_id = Column('users.id', Integer)


    def __init__(self, first_number, action, second_number, result, user_id):
        self.first_number = first_number
        self.action = action
        self.second_number = second_number
        self.result = result
        self.user_id = user_id


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column('User_name', String)
    counter = Column('Counter', Integer)

    def __init__(self, user_name, counter):
        self.user_name = user_name
        self.counter = counter
