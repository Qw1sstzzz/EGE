def f(x, y, A):
    return (x <= A) or (y < A) or (x + 2*y > 50)

for a in range(0, 10_000):
    if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break

# 17