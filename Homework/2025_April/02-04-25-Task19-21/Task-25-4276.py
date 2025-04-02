def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def D(arr):
    if len(arr) < 7: return 0
    return arr[-7]

cnt = 0
for x in range(400_000_001, 10**10):
    divs = dell(x)
    d = D(divs)
    if d > 0:
        print(d, len(divs))
        cnt += 1
    if cnt == 5:
        break