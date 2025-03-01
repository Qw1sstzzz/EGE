def f(x, A):
    return (x % A == 0) or ((170 <= x <= 220) <= (x % 24 != 0))

cnt = 0
for A in range(1, 10_000):
    if all(f(x, A) for x in range(1, 10_000)):
        cnt += 1
print(cnt)