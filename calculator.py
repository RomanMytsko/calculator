import os.path
import psycopg2


class Calculator:
    actions = ["+", "-", "/", "*"]

    def __init__(self, first_number, second_number, action):
        self.first_number = first_number
        self.second_number = second_number
        self.action = action

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number

    def calculate(self):
        if self.action == "+":
            return self.addition()
        elif self.action == "-":
            return self.subtraction()
        elif self.action == "*":
            return self.multiplication()
        elif self.action == "/" and self.second_number != 0:
            return self.division()
        elif self.action == "/" and self.second_number == 0:
            result = None
            return result


def check_input_num(number):
    if number.isdigit():
        return float(number)
    else:
        print("Please try again")
        return False


def check_wish(wish):
    if wish == "y":
        read_results(table_name)
        return False
    elif wish == "n":
        return False
    else:
        print("Try again please! ")
        return True


def check_table(table_name):
    connection = psycopg2.connect(user="roma",
                                  password="thesoprano777",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="calculator_db")
    cursor = connection.cursor()
    cursor.execute("select * from information_schema.tables where table_name=%s", (table_name,))
    result_of_exist_table = bool(cursor.rowcount)
    cursor.close()
    connection.close()
    return result_of_exist_table


def create_table(table_name):
    connection = psycopg2.connect(user="roma",
                                  password="thesoprano777",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="calculator_db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE %s
                            (action_id SERIAL PRIMARY KEY,
                             first_number REAL NOT NULL, 
                             action TEXT NOT NULL,
                             second_number REAL NOT NULL, 
                             result REAL NOT NULL);''' % table_name)
    connection.commit()
    cursor.close()
    connection.close()


def input_results():
    connection = psycopg2.connect(user="roma",
                                  password="thesoprano777",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="calculator_db")
    cursor = connection.cursor()

    cursor.execute(
        '''INSERT INTO calculator (first_number, action, second_number, result) VALUES (%s,%s,%s,%s);''',
        (our_example.first_number, our_example.action, our_example.second_number, round(our_example.calculate(), 4)))
    connection.commit()
    cursor.close()
    connection.close()


def read_results(table_name):
    connection = psycopg2.connect(user="roma",
                                  password="thesoprano777",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="calculator_db")
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

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":

    table_name = "calculator"
    if not check_table(table_name):
        create_table(table_name)

    again = "y"
    while again == "y":

        print("Do you want to see history? (y/n)")
        var = 1
        while var:
            var = check_wish(input())

        print("Please enter the first number: ")
        number = 1
        while number:
            first_number = check_input_num(input())
            if type(first_number) == float:
                break
            else:
                continue

        print("Please enter the second number: ")
        while True:
            second_number = check_input_num(input())
            if type(second_number) == float:
                break
            else:
                continue

        print("Please, enter action to do: ", Calculator.actions)

        while True:
            action = input()
            if action not in Calculator.actions:
                print("This is not a mathematical action please, try again:")
                continue
            else:
                break

        our_example = Calculator(first_number, second_number, action)

        if our_example.calculate():
            print("Your result is: ", round(our_example.calculate(), 4))
            input_results()
        else:
            print("It's not possible to divide by zero!")

        print("Do you want to continue? (y/n)")

        while True:
            again = (input())
            if again == "y" or again == "n":
                break
            else:
                print("Try again !")
                continue
