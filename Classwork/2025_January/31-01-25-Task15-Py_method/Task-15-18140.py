def f(x, y, A):
    return ((x - y) >= 39) or (y <= x) or (y >= (A - 20))

for A in range(0, 10_000)[::-1]:
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break

# 22