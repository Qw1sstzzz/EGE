ans = []

for N in range(1, 13):
    s = bin(N)[2:]
    if s[-1] == '0':
        s = '10' + s
    else:
        s = '1' + s + '01'
    R = int(s, 2)
    if N <= 12:
        ans.append(R)
print(max(ans))