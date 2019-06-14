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

counter = 1
while counter:
    try:
        first_number = float (input ("Please enter first number: "))
        counter = 0
    except ValueError as mistake:
        print ("You entered not number, please try again:")
        counter = 1
counter = 1
while counter:
    try:
        second_number = float (input ("Please enter second number: "))
        counter = 0
    except ValueError as mistake:
        print ("You entered not number, please try again:")
        counter = 1

actions = "+-/*"
counter = 1
while counter:
    action = input ("Please enter action to do ( + or - or * or /): ")
    if action not in actions:
        print ("You entered not correct action, please try again:")
        counter = 1
    else:
        break

our_example = Calculator(first_number,second_number, action)

if our_example.action == "+":
    result = our_example.addition()
elif our_example.action == "-":
    result = our_example.subtraction()
elif our_example.action == "*":
    result = our_example.multiplication()
else:
    result = our_example.division()
print("Your result is: ", result)




