from fnmatch import fnmatch

def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0: r |= {i, num//i}
    return sorted(r)

def uniq(arr):
    cnt, summ = 0, 0
    for i in arr:
        if fnmatch(str(i), '*7?'):
            cnt += 1
            summ += i
    if cnt >= 18:
        return summ
    return 0


for x in range(400_000, 500_001):
    divs = dell(x)
    osob = uniq(divs)
    if osob != 0:
        print(x, osob)