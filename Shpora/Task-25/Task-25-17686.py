def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def last_7(arr):
    ans = []
    for i in arr:
        if i == 7:
            continue
        if i % 10 == 7:
            ans.append(i)
    if len(ans) >= 1:
        return ans
    return 0

cnt = 0
for x in range(700_001, 10**10):
    divs = dell(x)
    l7 = last_7(divs)
    if l7 != 0:
        print(x, min(l7))
        cnt += 1
    if cnt == 5:
        break

