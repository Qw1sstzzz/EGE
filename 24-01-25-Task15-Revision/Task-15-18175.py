def f(x, A):
    return ((not (x % 7 == 0)) and (x % 13 == 0)) <= (x > (A - 40))

for A in range(1, 10_000)[::-1]:
    if all(f(x, A) for x in range(1, 10000)):
       print(A)
       break

# 52