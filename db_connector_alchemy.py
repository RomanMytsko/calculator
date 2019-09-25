from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.orm import sessionmaker
from connection import config
from models import Results, Base

database = "calculator_db"
conf = ('postgresql://{}:{}@{}/{}'.format(config["user"], config["password"], config["host"], database))
engine = create_engine(conf)

Session = sessionmaker(bind=engine)

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
