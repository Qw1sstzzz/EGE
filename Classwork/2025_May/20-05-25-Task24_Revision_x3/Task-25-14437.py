def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if len(arr) == 0:
        return 0
    return int(sum(arr) / len(arr))

cnt = 0
for x in range(1, 700_000)[::-1]:
    divs = dell(x)
    m = M(divs)
    if str(m)[-3:] == '313':
        print(x, m)
        cnt += 1
    if cnt == 7:
        break