def f(x, y, A):
    return ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or (y**2 + 7*y + 12 > 0))

cnt = 0

for A in range(-10, 500):
    if all(f(x, y, A) for x in range(-100, 100) for y in range(-100, 100)):
        cnt += 1
print(cnt)