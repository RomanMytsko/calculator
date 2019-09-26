from sqlalchemy import Column, String, Integer, Date, create_engine
# from base_alchemy import Base, engine, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connection import config

database = "calculator_db"
conf = ('postgresql://{}:{}@{}/{}'.format(config["user"], config["password"], config["host"], database))
engine = create_engine(conf)

Session = sessionmaker(bind=engine)

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


Base.metadata.create_all(engine)
session = Session()


def add_res(results):
    session.add(results)
    session.commit()
    session.close()


def read_res():
    results = session.query(Results).all()
    for result in results:
        print(str(result.id) + '.', result.first_number, result.action, result.second_number, ' = ', result.result)
    session.close()



