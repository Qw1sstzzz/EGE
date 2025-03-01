ans = []
for N in range(1, 10_000):
    s = bin(N)[2:]
    if s.count('0') % 2 == 0:
        s = '1' + s + '1'
    else:
        s = '10' + s
    R = int(s, 2)
    if R < 100:
        ans.append(R)
print(max(ans))