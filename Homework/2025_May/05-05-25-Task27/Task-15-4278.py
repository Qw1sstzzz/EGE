def f(x, A):
    return (A % 12 == 0) and ((530 % x == 0) <= ((A % x != 0) <= (170 % x != 0)))

cnt = 0
for A in range(1, 1_001):
    if all(f(x, A) for x in range(1, 10_000)):
        cnt += 1
print(cnt)