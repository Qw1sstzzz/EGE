def f(x, y, A):
    return ((x*y) < A) or (x < y) or (9 < x)

for A in range(0, 1000):
    if all(f(x, y, A) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

# 82