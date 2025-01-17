ans = []
for N in range(1, 100):
    s = bin(N)[2:]
    if N % 2 != 0: s = '10' + s + '1'
    else: s = '10' + s + '0111'
    R = int(s, 2)
    if N <= 25:
        ans.append(R)
print(max(ans))

# 1415