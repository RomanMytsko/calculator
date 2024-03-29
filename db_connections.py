import psycopg2
from connection import config
import json


class Database:

    def __init__(self):
        self.connection = psycopg2.connect(user=config["user"],
                                           password=config["password"],
                                           host=config["host"],
                                           port=config["port"],
                                           database="calculator_db")

    def create_table(self, table_name):

        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE %s
                                (action_id SERIAL PRIMARY KEY,
                                 first_number REAL NOT NULL, 
                                 action TEXT NOT NULL,
                                 second_number REAL NOT NULL, 
                                 result REAL NOT NULL,
                                 user_id INTEGER );
                                 ''' % table_name)
        self.connection.commit()

    def check_table(self, table_name):

        cursor = self.connection.cursor()
        cursor.execute("select * from information_schema.tables where table_name=%s", (table_name,))
        result_of_exist_table = bool(cursor.rowcount)

        return result_of_exist_table

    def input_results(self, calculator):
        cursor = self.connection.cursor()

        cursor.execute(
            '''INSERT INTO calculator (first_number, action, second_number, result) VALUES (%s,%s,%s,%s);''',
            (

                calculator.first_number, calculator.action, calculator.second_number, round(calculator.calculate(), 4)))
        self.connection.commit()

    def read_results(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(
            '''SELECT * FROM %s''' % table_name)
        table_records = cursor.fetchall()
        if len(table_records) > 0:
            res = []
            for i in table_records:
                for t in i:
                    res.append(str(t))
                res_string = ' '.join(res)
                print(res_string)
                res = []
        else:
            print("You have no history")

    def close_connection(self):
        cursor = self.connection.cursor()
        cursor.close()
        self.connection.close()
