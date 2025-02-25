def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def last_7(arr):
    ans = []
    for i in arr:
        if i != 7 and i % 10 == 7:
            ans.append(i)
    return ans

cnt = 0
for x in range(700_001, 10**10):
    divs = dell(x)
    if last_7(divs):
        mini = min(last_7(divs))
        print(x, mini)
        cnt += 1
    if cnt == 5:
        break