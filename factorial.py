# factorial
def factorial(n):
    # calculates the factorial of a non negative integer n
    # Args
    # n a non-negative number
    # Returns
    # The factorial of n

    if n == 0:
        return 1
    else:
        return n * (n-1)


number = 25
result = factorial(number)
print(f"Factorial of {number} is {result}")
