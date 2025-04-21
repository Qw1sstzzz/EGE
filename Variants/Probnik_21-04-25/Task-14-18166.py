def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for x in range(2, 2026):
    n = 5**2025 + 5**200 - x
    s = convert(n, 5)
    ans.append([s.count('4'), x])
print(max(ans))