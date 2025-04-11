def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]
ans = []
for N in range(1, 10_000):
    s = convert(N, 3)
    if N % 5 == 0:
        s += s[-3:]
    else:
        s += convert(N % 5 * 5, 3)

    R = int(s, 3)
    if R < 5496:
        ans.append(N)
print(max(ans))
