def dell(num):
    r = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if len(arr) < 1:
        return 0
    else:
        R = 0
        for k in arr:
            R += k
        return R // len(arr)

cnt = 0
for x in range(700_000, 1, -1):
    divs = dell(x)
    m = M(divs)
    if str(m)[-3:] == '313':
        print(x, m)
        cnt += 1
    if cnt == 7:
        break