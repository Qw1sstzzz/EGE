from fnmatch import fnmatch

def dell(num):
    r = set()
    for i in range(1, int(num**0.5)+ 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def f(arr):
    ans = []
    for i in arr:
        if fnmatch(str(i), '4*'):
            ans.append(i)
    if len(ans) == 24:
        return max(ans)
    return 0

for x in range(1, 10**6):
    divs = dell(x)
    if f(divs):
        print(x, f(divs))