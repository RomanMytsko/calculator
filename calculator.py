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

print("Do you want to see the last 10 actions? y/n")
my_choice_of_see_last_options = input()
if my_choice_of_see_last_options == "y":
    with open ("results.txt", "r") as results:
        counter = 1
        for l in results:
            print (l)
            counter += 1
            if counter > 10:
                break

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


with open("results.txt","a") as results:
    results.write(str(our_example.first_number) + " " + str(our_example.action) + " " + str(our_example.second_number) + " = " + str(our_example.calculate()) + "; " + "\n")


print ("Your result is: ", our_example.calculate ())