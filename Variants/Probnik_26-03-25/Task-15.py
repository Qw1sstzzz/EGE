def f(x, y, A):
    return ((x + 2) <= 50) or (y < (x + 10)) or (x >= A)

for A in range(1, 1_000)[::-1]:
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break