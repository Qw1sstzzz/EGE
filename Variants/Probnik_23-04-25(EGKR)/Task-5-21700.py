def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for N in range(3, 10_000):
    s = convert(N, 3)
    if N % 3 == 0: s += s[-2:]
    else: s += convert(N % 3 * 3, 3)
    R = int(s, 3)
    if R <= 150:
        ans.append([N, R])
print(max(ans))