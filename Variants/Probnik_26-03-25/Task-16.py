from functools import lru_cache

def f(n):
    if n <= 3: return n
    if n > 3: return (n - 2)*f(n-2)

for i in range(4, 1025):
    f(i)

print((f(1024) + 2*(f(1024) - f(1022))) // f(1020))