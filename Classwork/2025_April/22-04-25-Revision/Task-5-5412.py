ans = []
for N in range(1, 10_000):
    s = hex(N)[2:].upper()
    if s.count('B') % 2 == 0:
        s = '1' + s
    else:
        s += '1'
    R = int(s, 16)
    if 10 <= R <= 99:
        ans.append(N)
print(len(ans))