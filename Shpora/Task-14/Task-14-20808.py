ans = []
for x in range(1, 2031):
    num = 7**170 + 7**100 - x
    cnt0 = 0
    while num:
        if num % 7 == 0:
            cnt0 += 1
        num //= 7
    ans.append([cnt0, x])

ans = sorted(ans, key=lambda x: (-x[0], -x[1]))

print(ans[0][1])