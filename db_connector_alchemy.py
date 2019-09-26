from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.orm import sessionmaker
from connection import config
from models import Results, Base

database = "calculator_db"
conn_str = ('postgresql://{}:{}@{}/{}'.format(config["user"], config["password"], config["host"], database))


class SQLAlchemyDBConnection(object):

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)
        Session = sessionmaker()
        self.session = Session(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def read_res():
    with SQLAlchemyDBConnection(conn_str) as db:
        results = db.session.query(Results).all()
        for result in results:
            print(str(result.id) + '.', result.first_number, result.action, result.second_number, ' = ', result.result)


def add_res(results):
    with SQLAlchemyDBConnection(conn_str) as db:
        db.session.add(results)
        db.session.commit()
