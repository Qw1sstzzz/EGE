

for N in range(1, 10_000)[::-1]:
    s = oct(N)[2:]

    if N % 2 == 0: s += str(max(int(i) for i in s))
    else: s  += oct(min(int(i) for i in s) * 2)[2:]

    R = int(s, 8)
    if R < 313:
        print(N)
        break

# 38