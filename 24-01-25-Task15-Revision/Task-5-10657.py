def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

res = []
for N in range(1, 10_000):
    s = convert(N, 3)
    summi = sum(map(int, s))
    if summi % 3 == 0: s = '20' + s
    else: s = '10' + s
    R = int(s, 3)
    if R < 100:
        res.append(N)
print(max(res))