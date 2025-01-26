def f(x, y, A):
    return (x + y <= 30) or (y <= x + 2) or (y >= A)

for A in range(0, 1000)[::-1]:
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break