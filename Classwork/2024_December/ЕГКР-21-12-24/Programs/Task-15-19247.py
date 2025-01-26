def f(x, y, a):
    return ((x - 3*y) < a) or (y > 400) or (x > 56)

for a in range(0, 10_000):
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break

# 54