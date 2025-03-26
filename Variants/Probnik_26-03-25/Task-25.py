def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if len(arr) < 2: return 0
    return max(arr) - min(arr)

cnt = 0
for x in range(300_001, 10**10):
    divs = dell(x)
    m = M(divs)
    if m % 10 == 6:
        print(x, m)
        cnt += 1
    if cnt == 5:
        break
