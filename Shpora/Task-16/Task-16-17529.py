from functools import lru_cache

@lru_cache(9999)

def f(n):
    if n == 1: return 1
    return n*f(n-1)

for i in range(2, 2025):
    f(i)

print((2*f(2024) + f(2023)) // f(2022))