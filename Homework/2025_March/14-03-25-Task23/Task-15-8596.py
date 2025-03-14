def f(x, y, A):
    return (x >= 11) or (3*x < y) or (x*y < A)

for A in range(0, 10_000):
    if all(f(x, y, A) for x in range(0, 1_000) for y in range(0, 1_000)):
        print(A)
        break