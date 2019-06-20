class Calculator:

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
        elif self.action == "/":
            return self.division()

def check_input_num(action_description):
    print (action_description)
    while ValueError:
        try:
            float_number = float(input())
            break
        except ValueError:
            print ("It's not a number please try again:")
    return float_number

first_number = check_input_num("Please enter the first number: ")
second_number = check_input_num("Please enter the second number: ")

actions = "+-/*"
print("Please enter action to do: ", actions)
while True:
    action = input()
    if action not in actions:
        print ("This is not a mathematical action please try again:")
        continue
    else:
        break

our_example = Calculator(first_number, second_number, action)

print("Your result is: ", our_example.calculate())


