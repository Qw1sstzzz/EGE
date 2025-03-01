def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if len(arr) < 1: return 0
    return max(arr) + min(arr)

cnt = 0
for x in range(220_001, 10**10):
    divs = dell(x)
    m = M(divs)
    if str(m)[-1] == '4':
        print(x, m)
        cnt += 1
    if cnt == 5:
        break