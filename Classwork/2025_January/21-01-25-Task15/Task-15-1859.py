def f(x, y, A):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(0, 1000)[::-1]:
    if all(f(x, y, A) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break