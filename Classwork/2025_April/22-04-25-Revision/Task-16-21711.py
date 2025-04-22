from sys import setrecursionlimit
setrecursionlimit(9999)
def f(n):
    if n < 20: return n
    if n >= 20: return (n - 6) * f(n-7)

# for i in range(47856, 47873, 1):
#     f(i)

print((f(47872) - 290*f(47865))//f(47858))