import time

def fib_iterative(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    
    n1 = 1
    n2 = 1

    for i in range(n - 2):
        n1, n2 = n2, n1 + n2

    return n2

start = time.time()
print(fib_iterative(20))
end = time.time()
print(f"Time: {end - start}")