from fnmatch import fnmatch

def dell(num):
    ans = set()
    for x in range(1, int(num**0.5) + 1):
        if num % x == 0:
            ans.add(x)
            ans.add(num//x)
    return list(ans)

cnt = 0
for x in range(10000, 10**7):
    if fnmatch(str(x), '?6*6*?6'):
        if (x % 6 == 0) and (x % 7 == 0) and (x % 8 == 0):
            print(x, sum(dell(x)))
            cnt += 1
        if cnt == 7:
            break