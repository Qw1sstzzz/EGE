from functools import lru_cache
@lru_cache(None)

def f(n):
    if n < 3: return 3
    if n >= 3: return 2*n + 5 + f(n-2)

for i in range(3, 3027):
    f(i)

print(f(3027) - f(3023))