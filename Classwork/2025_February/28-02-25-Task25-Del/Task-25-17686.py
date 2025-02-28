def dell(num):
    r = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def f(arr):
    ans = []
    for i in arr:
        if i != 7 and i % 10 == 7:
            ans.append(i)
    if len(ans) < 1:
        return False
    return ans[0]

cnt = 0
for x in range(700_001, 10**10):
    divs = dell(x)
    last_7 = f(divs)
    if last_7 != 0:
        print(x, last_7)
        cnt += 1
    if cnt == 5:
        break