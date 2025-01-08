def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

res = []
for N in range(11, 10_000):
    s = convert(N, 3)
    chet = len([i for i in s if int(i) % 2 == 0])
    nechet = len([i for i in s if int(i) % 2 != 0])
    if chet > nechet: s = '22' + s
    else: s = '11' + s
    R = int(s, 3)
    if R > 100:
        res.append(R)
print(min(res))

# 120