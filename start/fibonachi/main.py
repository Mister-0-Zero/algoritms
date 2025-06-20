import time

def fib_recursive(n: int) -> int:
    if n <= 0: 
        raise  ValueError("the number must be more zero")
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

start = time.time()
print(fib_recursive(123))
end = time.time()
print(f"Time: {end - start}")

def fib_iterative(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    
    n1 = 1
    n2 = 1

    for i in range(n - 2):
        n1, n2 = n2, n1 + n2

    return n2

start = time.time()
print(fib_iterative(123))
end = time.time()
print(f"Time: {end - start}")