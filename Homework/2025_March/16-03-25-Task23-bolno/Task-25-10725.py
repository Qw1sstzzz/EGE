from fnmatch import fnmatch

def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i % 2 == 0: r |= {i}
            if (num // i) % 2 == 0: r |= {num//i}
    return sorted(r)

def length(arr):
    if len(arr) < 4: return 0
    return sum(arr)

cnt = 0
for x in range(65001, 10**10):
    divs = dell(x)
    if length(divs):
        if fnmatch(str(x), '6*97*5?'):
            print(x, length(divs))
            cnt += 1
    if cnt == 7:
        break



