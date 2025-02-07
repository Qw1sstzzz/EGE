def f(x, A):
    return (x & 1097 == 0) <= ((x & 2047 != 0) <= (x & A != 0))

for A in range(1, 10_000):
    if all(f(x, A) for x in range(1, 10_000)):
        print(A)
        break