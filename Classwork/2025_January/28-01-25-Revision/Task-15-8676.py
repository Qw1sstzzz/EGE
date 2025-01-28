def f(x, B):
    return (((x & 500) != 0) and ((x & 200) == 0)) <= (not ((x & B) == 0))

for B in range(0, 10_000):
    if all(f(x, B) for x in range(0, 10_000)):
        print(B)
        break