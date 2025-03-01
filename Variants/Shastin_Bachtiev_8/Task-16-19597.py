from functools import *

@lru_cache(None)

def f(n):
    if n < 15: return 4
    if n >= 15 and (n % 3 == 0): return f(2* n // 3) + n - 1
    if n >= 15 and (n % 3 != 0): return f(n - 1) + 3

for i in range(16, 5_000):
    f(i)

for n in range(16, 10_000)[::-1]:
    if f(n) == 251:
        print(n)
        break