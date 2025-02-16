from fnmatch import fnmatch

def dell(num):
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num // i)
    return divs

for x in range(7777, 10**10 + 1, 7777):
    if fnmatch(str(x),'12*567?'):
        min_del = min(dell(x))
        max_del = max(dell(x))
        if (min_del + max_del) % 2 != 0:
            print(x, x // 7777)

