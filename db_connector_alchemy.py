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

    def read_user_before_save(self, our_user):
        users = self.db.session.query(Users).all()
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

    def read_user(self, our_user):
        for user in self.db.session.query(Users).all():
            if our_user == user.user_name:
                id_to_results = user.id
                return id_to_results

    def update_counter(self, our_user_id):
        if our_user_id:
            users = self.db.session.query(Users).get(our_user_id)
            users.counter += 1
            self.db.session.commit()

    def output_user_actions_count(self, our_user):
        var = False
        for user in self.db.session.query(Users).all():
            if our_user == user.user_name:
                str_to_print = " you did {} actions before!".format(user.counter)
                print(our_user, str_to_print)
                var = True
        if not var:
            str_to_print = ", you didn't do any actions before!"
            print(our_user, str_to_print)
        return str_to_print

