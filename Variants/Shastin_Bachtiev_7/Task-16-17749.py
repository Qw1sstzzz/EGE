from functools import *
@lru_cache(None)

def f(n):
    if n > 7000: return n + 4
    if n <= 7000: return 3*n + 5 + f(n+3)

for i in range(7002, 706, -1):
    f(i)

print(f(707) - f(716))
# 6405