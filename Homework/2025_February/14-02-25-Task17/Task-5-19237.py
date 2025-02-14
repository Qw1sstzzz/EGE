def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

res = []
for N in range(1, 10_000):
    s = convert(N, 3)
    if N % 3 == 0: s += s[-2:]
    else:
        summi = sum(map(int, s))
        s += convert(summi, 3)
    R = int(s, 3)
    if R > 220:
        res.append(R)
print(min(res))