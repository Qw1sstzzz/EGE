from functools import lru_cache

@lru_cache(9999)

def f(n):
    if n == 1: return 1
    return (n - 1)*f(n - 1)

for i in range(2, 2025):
    f(i)

print((f(2024)//7 - f(2023)) // f(2022))