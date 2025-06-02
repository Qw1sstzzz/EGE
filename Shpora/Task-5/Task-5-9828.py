from string import digits, ascii_uppercase

def convert(num, sys):
    alph = digits + ascii_uppercase
    r = ''
    while num:
        r += alph[num % sys]
        num //= sys
    return r[::-1]

ans = []

for N in range(1, 10_000):
    s = convert(N, 3)
    if N % 3 == 0: s = '1' + s + '02'
    else: s += convert(N % 3 * 4, 3)
    R = int(s, 3)
    if R < 199:
        ans.append(N)

print(max(ans))