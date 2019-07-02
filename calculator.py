import os.path


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


def check_wish(wish):
    if wish == "y":
        with open("results.txt", "r") as results:
            for line in results:
                print(line)
        return False
    elif wish == "n":
        return False
    else:
        print("Try again please! ")
        return True


if not os.path.isfile("results.txt"):
    results = open("results.txt", "w")
    results.close()

print ("Do you want to see history? (y/n)")
var = 1
while var:
    var = check_wish(input())

counter = 1
while counter:
    try:
        first_number = float(input("Please, enter first number: "))
        counter = 0
    except ValueError as mistake:
        print("You entered not number, please, try again:")
        counter = 1
counter = 1
while counter:
    try:
        second_number = float(input("Please, enter second number: "))
        counter = 0
    except ValueError as mistake:
        print("You entered not number, please, try again:")
        counter = 1

actions = "+-/*"
counter = 1
while counter:
    action = input("Please, enter action to do ( + or - or * or /): ")
    if action not in actions:
        print("You entered not correct action, please, try again:")
        counter = 1
    else:
        break

our_example = Calculator (first_number, second_number, action)

if our_example.action == "+":
    result = our_example.addition()
elif our_example.action == "-":
    result = our_example.subtraction()
elif our_example.action == "*":
    result = our_example.multiplication()
else:
    result = our_example.division()
print("Your result is: ", round(result, 4))

with open("results.txt", "a") as results:
    results.write(str(our_example.first_number) + " " + str(our_example.action) + " " + str(
        our_example.second_number) + " " + "=" + " " + str(result) + '\n')

with open("results.txt", "r") as file:
    lines = file.readlines()
    if len(lines) > 10:
        del lines[0]

with open("results.txt", "w") as file:
    file.writelines(lines)
