def f(y, x, A):
    return (y > 10) or ((x*A) > (y + x))

for A in range(1, 10_000):
    if all(f(y, x, A) for x in range(1, 1_000) for y in range(1, 1_000)):
        print(A)
        break