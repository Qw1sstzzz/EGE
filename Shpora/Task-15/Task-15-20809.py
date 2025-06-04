def f(x, A):
    B = 60 <= x <= 80
    return ((x % A) == 0) or (B <= ((x % 22) != 0))

for A in range(1000, 1, -1):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break