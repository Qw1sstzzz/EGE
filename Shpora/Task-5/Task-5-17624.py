ans = []
for N in range(1, 10_000):
    s = bin(N)[2:]
    s += str(sum(map(int, s)) % 2)
    s += str(sum(map(int, s)) % 2)
    R = int(s, 2)
    if R > 75:
        ans.append(R)

print(min(ans))