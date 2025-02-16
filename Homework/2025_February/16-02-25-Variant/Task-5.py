def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

res = []
for N in range(1, 10_000):
    s = convert(N, 4)
    if len(s) % 2 == 0:
        s = s[:len(s)//2] + '0' + s[len(s)//2:]
    R = int(s)
    if R <= 180:
        res.append([N, R])
print(max(res))