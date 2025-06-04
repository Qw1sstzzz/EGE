ans = []
for x in range(1, 3001):
    n = 4**210 + 4**110 - x
    cnt0 = 0
    while n:
        if n % 4 == 0:
            cnt0 += 1
        n //= 4
    ans.append([cnt0, x])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans[0][1])