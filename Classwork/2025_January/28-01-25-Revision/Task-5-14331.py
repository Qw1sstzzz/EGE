def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for N in range(1, 10_000):
    s = convert(N, 3)
    summi = sum([int(i) for i in s])
    if summi % 3 == 0: s += '212'
    else: s += convert(summi * 2, 3)
    R = int(s, 3)
    if R > 490:
        ans.append(R)
print(min(ans))

# 512