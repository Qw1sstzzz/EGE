def f(x, A):
    return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))

for A in range(1, 10_000)[::-1]:
    if all(f(x, A) for x in range(1, 10_000)):
        print(A)
        break