import os.path
import psycopg2
import re
import db_connector_alchemy as session
from models import Results, Users


class Calculator:
    actions = ['+', '-', '/', '*']

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
        if self.action == '+':
            return self.addition()
        elif self.action == '-':
            return self.subtraction()
        elif self.action == '*':
            return self.multiplication()
        elif self.action == '/' and self.second_number != 0:
            return self.division()
        elif self.action == '/' and self.second_number == 0:
            result = None
            return result


def check_input_num(number):
    if number.isdigit():
        return float(number)
    else:
        print("Please try again")
        return False


def check_wish(wish):
    if wish == 'y':
        session.read_res()
        return False
    elif wish == 'n':
        return False
    else:
        print('Try again please! ')
        return True


def user_input():
    user = input("Please enter your name >  ")
    return user


def parse_expression(my_string):
    my_regex = r'(^-?\d+[.]?\d+|^-?\d+)([{}])(-?\d+[.]?\d+$|-?\d+$)'.format(''.join(Calculator.actions))
    result = re.match(my_regex, my_string)

    if result:
        first_number = float(result.group(1))
        action = result.group(2)
        second_number = float(result.group(3))
        return first_number, second_number, action
    else:
        print("Try again")
        return False


if __name__ == "__main__":

    table_name = 'calculator'
    again = 'y'

    while again == 'y':

        alchemy_actions = session.AlchemyActions()
        our_user = user_input()
        alchemy_actions.output_user_actions_count(our_user)
        our_user_id = alchemy_actions.user_id(our_user)
        if alchemy_actions.user_in_table(our_user):
            alchemy_actions.update_counter(our_user)
        else:
            our_user_to_table = Users(our_user, 1)
            alchemy_actions.add_user(our_user_to_table)

        print('Do you want to see history? (y/n)')
        var = 1
        while var:
            var = check_wish(input())
        print("Please input first number, action and second number: ")
        first_number = False
        while not first_number:
            my_string = input()
            if parse_expression(my_string):
                first_number, second_number, action = parse_expression(my_string)
                break
            else:
                continue

        our_example = Calculator(first_number, second_number, action)

        if our_example.calculate():
            print("Your result is: ", round(our_example.calculate(), 4))

            to_alchemy_results = Results(first_number, action, second_number,
                                         our_example.calculate(), our_user_id)

            alchemy_actions.add_res(to_alchemy_results)
        else:
            print("It's not possible to divide by zero!")

        print("Do you want to continue? (y/n)")

        while True:
            again = (input())
            if again == "y":
                break
            elif again == "n":
                break
            else:
                print("Try again !")
                continue
