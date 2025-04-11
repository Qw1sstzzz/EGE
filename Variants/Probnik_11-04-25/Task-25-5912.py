from fnmatch import fnmatch

def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {num//i, i}
    return sorted(r)

for x in range(12045, 10**7 + 1):
    divs = dell(x)
    if len(divs) == 18 and fnmatch(str(x), '12?*45'):
        print(x, divs[-1])