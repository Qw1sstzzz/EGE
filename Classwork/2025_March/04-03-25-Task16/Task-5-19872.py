def convert(num):
    r = ''
    while num:
        r += str(num % 7)
        num //= 7
    return r[::-1]

ans = []
for N in range(1, 1_000):
    s = convert(N)
    if N % 2 == 0:
        s = '52' + s + '1'
    else:
        first = s[0]
        last = s[-1]
        s = last + s[1:-1] + first + '15'
        while '0' == s[0]:
            s = s[1:]
    if len(s) == 4:
        ans.append([N, s])
print(*max(ans))