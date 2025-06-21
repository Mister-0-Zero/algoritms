import time

def fib_memo(n: int, cache: dict = None) -> int:
    if n < 1:
        raise ValueError("n должно быть больше или равном единице")
    if cache is None:
        cache = {}
    if n in (1, 2):
        cache[n] = 1
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

start = time.time()
print(fib_memo(20))
end = time.time()
print(f"Time: {end - start}")