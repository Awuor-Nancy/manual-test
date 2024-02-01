# write a program tat adds two numbers and retuns the result.
def add_two_numbers(num1, num2):
    return num1 + num2


# request input from users
num1 = int(input("Input num1: "))
num2 = int(input("Input num2: "))

# initialize a result variable
results = (add_two_numbers(num1, num2))
print(f"The output of {num1} and {num2} is {results}")
