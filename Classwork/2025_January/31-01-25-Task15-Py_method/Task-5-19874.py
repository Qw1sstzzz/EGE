def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for N in range(10, 1000):
    s = convert(N, 3)
    if N % 4 == 0: s += s[-3:]
    else: s = '1' + s + '20'

    R = int(s, 3)
    if R > 423:
        ans.append(R)

print(min(ans))

# 438