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
            print("It's not possible to divide by zero")
            return False


def check_input_num(number):
    if number.isdigit():
        return float(number)
    else:
        print("Please try again")
        return False


if __name__ == "__main__":

    again = "y"
    while again == "y":

        print("Please enter the first number: ")
        while True:
            first_number = check_input_num(input ())
            if first_number or first_number == 0:
                break
            else:
                continue

        print ("Please enter the second number: ")
        while True:
            second_number = check_input_num(input())
            if second_number or second_number == 0:
                break
            else:
                continue

        print ("Please, enter action to do: ", Calculator.actions)

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
        print("Do you want to continue? (y/n)")

        while True:
            again = (input())
            if again == "y" or again == "n":
                break
            else:
                print("Try again !")
                continue



