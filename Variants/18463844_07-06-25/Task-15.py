def f(x, y, A):
    return (x*y < 100) or (y >= A) or (x > A)

for A in range(1000, -1, -1):
    if all(f(x, y, A) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break