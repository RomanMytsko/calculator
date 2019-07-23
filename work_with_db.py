import psycopg2


class Database_work:

    def create_table(connection, table_name):

        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE %s
                                (action_id SERIAL PRIMARY KEY,
                                 first_number REAL NOT NULL, 
                                 action TEXT NOT NULL,
                                 second_number REAL NOT NULL, 
                                 result REAL NOT NULL);''' % table_name)
        connection.commit()
        # cursor.close()
        # connection.close()

    def check_table(connection, table_name):

        cursor = connection.cursor()
        cursor.execute("select * from information_schema.tables where table_name=%s", (table_name,))
        result_of_exist_table = bool(cursor.rowcount)
        # cursor.close()
        # connection.close()
        return result_of_exist_table

    def input_results(connection, first_number, action, second_number, calculate):
        cursor = connection.cursor()

        cursor.execute(
            '''INSERT INTO calculator (first_number, action, second_number, result) VALUES (%s,%s,%s,%s);''',
            (
                first_number, action, second_number, round(calculate, 4)))
        connection.commit()
        # cursor.close()
        # connection.close()

    def read_results(connection, table_name):
        cursor = connection.cursor()
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
        # cursor.close()
        # connection.close()
