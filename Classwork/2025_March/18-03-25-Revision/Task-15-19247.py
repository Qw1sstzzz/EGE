def f(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(0, 10_000):
    if all(f(x, y, A) for x in range(1, 1_000) for y in range(1, 1_000)):
        print(A)
        break