def factorial(n):
    if n < 0:
        raise ValueError("No negative value")
    
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k

try:
    print(factorial(5))
    print(factorial(-1))
except ValueError as error_message:
    print(f"ValueError: {error_message}")