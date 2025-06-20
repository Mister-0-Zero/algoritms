def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("the number must be non-negative")
    
    output = 1
    for i in range(2, n + 1):
        output *= i
    
    return output

print(factorial(3))