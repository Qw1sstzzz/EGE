def f(x, A):
    return (x & 21074 != 0) <= ((x & 12369 == 0) <= (x & A != 0))

for A in range(0, 30000):
    if all(f(x, A) for x in range(0, 30000)):
        print(A)
        break