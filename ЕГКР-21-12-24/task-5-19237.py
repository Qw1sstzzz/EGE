def convert(num, sys):
    r = ''
    while num:
        r += str(num%sys)
        num //= sys
    return r[::-1]

res = []
for N in range(1, 10_000):
    s = convert(N, 3)
    if N % 3 == 0:
        s += s[-2:]
    else:
        sumi = sum(map(int, s))
        s += convert(sumi, 3)
    R = int(s, 3)
    if R % 2 == 0 and R > 220:
        res.append(R)
print(min(res))

# 222