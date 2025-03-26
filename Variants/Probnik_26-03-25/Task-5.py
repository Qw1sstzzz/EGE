def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for N in range(1, 10_000):
    s = convert(N, 4)
    summ = sum(map(int, s))
    if summ % 2 == 0:
        s += s[-2:]
    else:
        s = '2' + s + '0'
    R = int(s, 4)
    if R % 2 == 0 and R > 120:
        ans.append(R)
print(min(ans))