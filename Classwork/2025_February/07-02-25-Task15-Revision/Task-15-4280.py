def f(x, A):
    return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & A != 0) and (x & 58 == 0))

for A in range(43, 56)[::-1]:
    if all(f(x, A) == 0 for x in range(1, 10_000)):
        print(A)
        break