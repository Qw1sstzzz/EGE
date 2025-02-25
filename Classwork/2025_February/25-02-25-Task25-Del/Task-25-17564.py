def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if arr:
        return max(arr) + min(arr)
    return 0

cnt = 0
for x in range(700_001, 10_000_000):
    divs = dell(x)
    m = M(divs)

    if m % 10 == 4:
        print(x, m)
        cnt += 1
    if cnt == 5:
        break