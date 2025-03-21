def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]
ans = []
for N in range(1, 10_000):
    s = convert(N, 3)
    summ = sum(map(int, s))
    if summ % 2 == 0:
        s = '12' + s[2:] + '0'
    else:
        s = '10' + s[2:] + '2'
    R = int(s, 3)
    if R > 105:
        ans.append(N)
print(min(ans))