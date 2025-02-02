def f(x, A):
    return ((x & 57) == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 10_000):
    if all(f(x, A) for x in range(1, 10_000)):
        print(A)
        break

# 40