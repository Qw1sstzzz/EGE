def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]
ans = []
for N in range(1, 10_000):
    s = convert(N, 3)
    if sum(map(int, s)) % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    R = int(s, 3)
    if R > 100:
        ans.append(R)
print(min(ans))