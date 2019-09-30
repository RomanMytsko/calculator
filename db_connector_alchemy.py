from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.orm import sessionmaker
from connection import config
from models import Results, Base, Users

database = "calculator_db"
conn_str = ('postgresql://{}:{}@{}/{}'.format(config["user"], config["password"], config["host"], database))


class SQLAlchemyDBConnection(object):

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.session = None

    def __enter__(self):
        engine = create_engine(self.connection_string)
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        self.session = Session(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def read_res():
    with SQLAlchemyDBConnection(conn_str) as db:
        results = db.session.query(Results).all()
        for result in results:
            print(str(result.id) + '.', result.first_number, result.action, result.second_number, ' = ', result.result,
                  '_____', 'user >', result.user_id)


def add_res(results):
    with SQLAlchemyDBConnection(conn_str) as db:
        db.session.add(results)
        db.session.commit()


def add_user(user):
    with SQLAlchemyDBConnection(conn_str) as db:
        db.session.add(user)
        db.session.commit()


def read_user_before_save(our_user):
    with SQLAlchemyDBConnection(conn_str) as db:
        users = db.session.query(Users).all()
        if len(users) > 0:
            for user in users:
                if our_user == user.user_name:
                    our_user_id = user.id
                    break
                else:
                    our_user_id = 0
        else:
            our_user_id = 0
        return our_user_id


def read_user(our_user):
    with SQLAlchemyDBConnection(conn_str) as db:
        users = db.session.query(Users).all()
        for user in users:
            if our_user == user.user_name:
                id_to_results = user.id
                return id_to_results
