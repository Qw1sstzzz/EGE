from functools import lru_cache
@lru_cache(None)

def f(n):
    if n < 11: return n
    if n >= 11: return n + f(n-1)

for i in range(11, 2024):
    f(i)

print(f(2024) - f(2021))
