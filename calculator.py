import os.path
import psycopg2
from db_connections import Database


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
        cursor.read_results(table_name)
        return False
    elif wish == "n":
        return False
    else:
        print("Try again please! ")
        return True


if __name__ == "__main__":

    table_name = "calculator"
    cursor = Database()

    if not cursor.check_table(table_name):
        cursor.create_table(table_name)

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
            cursor.input_results(our_example)
            # cursor.our_calc = our_example
        else:
            print("It's not possible to divide by zero!")

        print("Do you want to continue? (y/n)")

        while True:
            again = (input())
            if again == "y":
                break
            elif again == "n":
                cursor.close_connection()
                break
            else:
                print("Try again !")
                continue
