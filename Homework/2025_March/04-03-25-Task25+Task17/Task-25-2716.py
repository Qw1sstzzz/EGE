def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def S(arr):
    if len(arr) < 3:
        return 0
    return sum(arr[-3:])

ans = []
cnt = 0
for x in range(1, 1_200_001)[::-1]:
    divs = dell(x)
    s = S(divs)
    if (s != 0) and (s % 2022 == 0) and (s != x):
        ans.append([x, s])
        cnt += 1
    if cnt == 5:
        break

ans = sorted(ans)

for i in ans:
    print(*i)