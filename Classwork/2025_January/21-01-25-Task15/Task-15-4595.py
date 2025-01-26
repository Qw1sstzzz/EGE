def f(x, a):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)

for a in range(1, 10_000):
    if all(f(x, a) for x in range(1, 10_000)):
        print(a)
        break

# 74