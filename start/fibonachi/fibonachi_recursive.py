import time

def fib_recursive(n: int) -> int:
    if n <= 0: 
        raise  ValueError("the number must be more zero")
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

start = time.time()
print(fib_recursive(20))
end = time.time()
print(f"Time: {end - start}")