def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for N in range(1, 10_000):
    s = convert(N, 5)
    if len(s) % 2 == 0:
        ch1 = s[:len(s) // 2]
        ch2 = s[len(s) // 2:]
        s = ch2 + ch1
    else:
        s += str(N % 5)
        ch1 = s[:len(s) // 2]
        ch2 = s[len(s) // 2:]
        s = ch2 + ch1
    R = int(s, 5)
    if R > 50:
        ans.append([N, R])
print(min(ans))