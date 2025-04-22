def f(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]
ans = []
for x in range(2, 2_025):
    n = 5**2025 + 5**200 - x
    s = f(n, 5)
    ans.append([s.count('4'), x])
print(max(ans))