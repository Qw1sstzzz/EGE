from string import digits, ascii_uppercase
def convert(num, sys):
    r = ''
    alph = digits + ascii_uppercase
    while num:
        r += alph[num % sys]
        num //= sys
    return r[::-1]

ans = []
for N in range(1, 10_000):
    s = convert(N, 12)
    if N % 3 == 0:
        s = '1' + s + 'B'
    else:
        s = '2' + s + '0'
    R = int(s, 12)
    if R < 1996:
        ans.append(R)

print(max(ans))
