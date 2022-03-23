# code to check that a number is valid

def temp_checker(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("Too Cold")
            else:
                return response

        except ValueError:
            print("Please enter a number: ")


# main routine
# set up to run this code twice (for two valid responses in test plan)
number = temp_checker(-273)
print("You entered {}".format(number))

number = temp_checker(-459)
print("You entered {}".format(number))