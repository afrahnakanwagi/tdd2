def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Testing the recursive function
for i in range(10):  # Fibonacci numbers for the first 10 indices
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")
