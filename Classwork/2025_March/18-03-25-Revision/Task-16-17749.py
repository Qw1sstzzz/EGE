from functools import lru_cache
@lru_cache(None)

def f(n):
    if n > 7_000: return n + 4
    if n <= 7_000: return 3*n + 5 + f(n+3)

for i in range(6999, 706, -1):
    f(i)

print(f(707) - f(716))