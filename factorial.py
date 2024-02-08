# factorial
def factorial(n):
    # calculates the factorial of a non negative integer n
    # Args
    # n a non-negative number
    # Returns
    # The factorial of n

    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
