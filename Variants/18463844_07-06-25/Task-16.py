from functools import lru_cache

@lru_cache(9999)

def f(n):
    if n <= 1: return 0
    if n > 1 and n % 2 != 0: return f(n-1) + 3*n**2
    if n > 1 and n % 2 == 0: return n // 2 + f(n-1) + 2

for i in range(2, 50):
    f(i)

print(f(49))