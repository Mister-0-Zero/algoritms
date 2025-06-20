import time

def fib_memo(n: int, cache: dict = None) -> int:
    if n == 1 or n == 2:
        return 1
    
    cache = {"1": 1, "2": 2}
    for i in range(3, n):
        cache[f"{i}"] = cache[f"{i - 2}"] + cache[f"{i - 1}"]

    return cache[f"{i}"]

start = time.time()
print(fib_memo(20))
end = time.time()
print(f"Time: {end - start}")