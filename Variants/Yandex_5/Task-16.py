from functools import *

@lru_cache(None)

def f(n):
    if n >= 2025: return 1
    else: return n - f(n+2) - f(n+4)

for i in range(2025, 19, -1):
    f(i)

print(f(20) + f(25))