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
                  '   ', 'user >', result.user_id)


class AlchemyActions:

    def __init__(self):
        with SQLAlchemyDBConnection(conn_str) as db:
            self.db = db

    def add_res(self, results):
        self.db.session.add(results)
        self.db.session.commit()

    def add_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def update_counter(self, our_user):
        for user in self.db.session.query(Users).all():
            if our_user == user.user_name:
                user.counter += 1
                self.db.session.commit()
                break

    def user_in_table(self, our_user):
        for users in self.db.session.query(Users.user_name).all():
            for user in users:
                if our_user == user:
                    return True

    def user_id(self, our_user):
        users = self.db.session.query(Users).all()
        if len(users) > 0:
            for user in users:
                if our_user == user.user_name:
                    user_id = user.id
                    break
                else:
                    user_id = len(users) + 1
            return user_id
        else:
            return 1

    def output_user_actions_count(self, our_user):
        var = False
        for user in self.db.session.query(Users).all():
            if our_user == user.user_name:
                str_to_print = " you did {} actions before!".format(user.counter)
                print(our_user, str_to_print)
                var = True
        if not var:
            return print(our_user, ", you didn't do any actions before!")
