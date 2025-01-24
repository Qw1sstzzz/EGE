def f(x, y, A):
    return not ((x < 7) or (y >= (3*x + A - 20)) or (x >= 34) or (y < 121))

for A in range(0, 1000)[::-1]:
    if all(f(x, y, A) == 0 for x in range(0, 1500) for y in range(0, 1500)):
        print(A)
        break