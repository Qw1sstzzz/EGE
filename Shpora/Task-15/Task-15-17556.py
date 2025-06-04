def f(x, A):
    B = 70 <= x <= 90
    return ((x % A) == 0) or (B <= ((x % 22) != 0))

for A in range(1, 1000)[::-1]:
    if all(f(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break