def f(x, A):
    return ((not (x % 5 == 0)) and (x % 4 == 0)) <= (x > (A - 11))


for A in range(1, 10_000)[::-1]:
    if all(f(x, A) for x in range(1, 10000)):
       print(A)
       break

# 14