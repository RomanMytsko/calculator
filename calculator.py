import os.path


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
            return self.addition ()
        elif self.action == "-":
            return self.subtraction ()
        elif self.action == "*":
            return self.multiplication ()
        elif self.action == "/" and self.second_number != 0:
            return self.division ()
        elif self.action == "/" and self.second_number == 0:
            print ("It's not possible to divide by zero")
            return False


def check_input_num(number):
    if number.isdigit():
        return float(number)
    else:
        print("Please try again")
        return False


def check_wish(wish):
    if wish == "y" and os.path.getsize("results.txt") > 0:
        with open("results.txt", "r") as results:
            for line in results:
                print(line)
        return False
    elif wish == "y" and os.path.getsize("results.txt") == 0:
        print("You have no history")
    elif wish == "n":
        return False
    else:
        print("Try again please! ")
        return True


if __name__ == "__main__":

    path_dir = str(os.path.dirname(os.path.abspath(__file__)))
    path_to_results = os.path.isfile(path_dir.join('/results.txt'))
    if not path_to_results:
        results = open("results.txt", "w")
        results.close()



    again = "y"
    while again == "y":

        print("Do you want to see history? (y/n)")
        var = 1
        while var:
            var = check_wish(input())

        print("Please enter the first number: ")
        while True:
            first_number = check_input_num(input())
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
        print("Do you want to continue? (y/n)")

        with open ("results.txt", "a") as results:
            results.write (str (our_example.first_number) + " " + str (our_example.action) + " " + str (
                our_example.second_number) + " " + "=" + " " + str (our_example.calculate ()) + '\n')

        with open ("results.txt", "r") as file:
            lines = file.readlines ()
            if len (lines) > 10:
                del lines[0]

        with open ("results.txt", "w") as file:
            file.writelines (lines)


        while True:
            again = (input())
            if again == "y" or again == "n":
                break
            else:
                print("Try again !")
                continue
