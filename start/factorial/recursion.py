def factorial(n: int, output: int = 1) -> int:
    if n < 0:
        raise ValueError("the number must be non-negative")
    elif n > 0:
        return factorial(n - 1, output * n)
    else:
        return output

print(factorial(3))