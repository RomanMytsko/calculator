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


    # def result(self):
    #     return eval(str(self.first_number) + str(self.action) + str(self.second_number))

def check_input_num(count_of_number):
    print (count_of_number)
    while ValueError:
        try:
            git float_number = float(input())
            break
        except ValueError:
            print ("You entered not number, please try again:")
    return float_number


first_number = check_input_num("Please enter the first number: ")
second_number = check_input_num("Please enter the second number: ")


actions = "+-/*"
print("Please enter action to do: ", actions)
while True:
    action = input()
    if action not in actions:
        print ("You entered not correct action, please try again:")
        continue
    else:
        break

our_example = Calculator(first_number, second_number, action)

if our_example.action == "+":
    result = our_example.addition()
elif our_example.action == "-":
    result = our_example.subtraction()
elif our_example.action == "*":
    result = our_example.multiplication()
else:
    result = our_example.division()
print("Your result is: ", result)