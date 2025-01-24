def f(x, A):
    return (A % x == 0) <= ((x == A) or (x == 1))

cnt = 0
for A in range(1, 11_112):
    if all(f(x, A) for x in range(1, 1000)):
        cnt += 1
print(cnt)