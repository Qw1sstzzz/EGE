def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]
ans = []
for x in range(1, 2031):
    s = 2**2025 + 2**2024 - 2**2021 - x
    n = convert(s, 4)
    ans.append([n.count('0'), x])
ans= sorted(ans)
print(max(ans))