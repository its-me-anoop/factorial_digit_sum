def factorial(num):
    """
    Calculates the factorial of a given number.

    Parameters:
    num (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def factorial_digit_sum(num):
    """
    Calculates the sum of the digits in the factorial of a given number.

    Parameters:
    num (int): The number for which the factorial digit sum is to be calculated.

    Returns:
    int: The sum of the digits in the factorial of the given number.
    """
    f = str(factorial(num))
    digit_sum = 0
    for digit in f:
        digit_sum += int(digit)
    return digit_sum


print(factorial_digit_sum(100))
