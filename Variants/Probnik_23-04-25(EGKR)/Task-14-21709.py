def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for x in range(1, 3000):
    n = 4**210 + 4**110 - x
    s = convert(n, 4)
    ans.append([s.count('0'), x])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans[:10])