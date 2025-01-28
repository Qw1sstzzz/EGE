def f(x, A):
    return ((x % 10 == 0) and (x % 26 == 0) and x >= 300) <= (A <= x)

for A in range(1, 10_000)[::-1]:
    if all(f(x, A) for x in range(1, 10_000)):
        print(A)
        break