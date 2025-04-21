from functools import *

@lru_cache(None)

def f(n):
    if n > 400: return n**n
    if n <= 400: return n + 6 + f(n+12)

for i in range(71, 401):
    f(i)

print(f(72) - f(108))