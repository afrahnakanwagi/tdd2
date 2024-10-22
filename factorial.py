def factorial(n):
    """Calculates the factorial of a non-negative integer.

     The factorial of a non-negative integer n, denoted by n!, is the product of
     all positive integers
    less than or equal to n. Mathematically,
    it can be
     expressed as:

     n! = 1 * 2 * 3 * ... * (n - 1) * n

     Args:
         n: The non-negative integer for which to calculate the factorial.

     Returns:
         The factorial of n. If n is negative, a ValueError is raised.

     Raises:
         ValueError: If n is a negative number.

     Examples:
         >>> factorial(5)
         120
         >>> factorial(0)
         1
         >>> factorial(-2)  # Will raise a ValueError
         Traceback (most recent call last):
             File "<stdin>", line 1, in <module>
         ValueError: Factorial is not defined for negative numbers
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Example usage: Calculate the factorial of 5.
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(3)) # Output: 6
# print(factorial(-2))  # Will raise a ValueError: Factorial is not defined for negative numbers
print(factorial(2)) #output: 2
print(factorial(4)) #output: 24
print(factorial(1)) #output: 1
# print(factorial(1000))

