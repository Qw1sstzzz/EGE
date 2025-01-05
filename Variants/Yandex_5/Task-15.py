def f(x, a):
    return ((not x % 100 == 0) and (x % 4 == 0)) or (x % 400 == 0) or (not x % a == 0)

for a in range(1, 10_000):
    if all(f(x, a) for x in range(0, 10_000)):
        print(a)
        break