ans = []
for N in range(1, 10_000):
    s = bin(N)[2:]
    s = s.replace('0', '*').replace('1', '0').replace('*', '1')
    s = '1' + s
    if s.count('1') % 2 == '0': s += '0'
    else: s += '1'
    R = int(s, 2)
    if R > 180:
        ans.append([N, R])
print(min(ans))