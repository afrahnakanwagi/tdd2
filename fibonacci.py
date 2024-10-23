#pair: Afrah & Aisha
"""def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)"""

# the code below
def fibonacci(n):  
    if n <= 0:  
        return []  
    elif n == 1:  
        return [0]  
    elif n == 2:  
        return [0, 1]  
    else:  
        sequence = [0, 1]  
        for i in range(2, n):  
            sequence.append(sequence[-1] + sequence[-2])  
        return sequence 
