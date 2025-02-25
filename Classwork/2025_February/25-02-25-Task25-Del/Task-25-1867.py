def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            r.add(i)
            r.add(num // i)
    return sorted(list(r))

def last_8(arr):
    r = []
    for i in arr:
        if (i != 8) and (i != arr[-1]) and (i % 10 == 8):
            r.append(i)
    return r

cnt = 0
for x in range(500001, 1_000_000):
    divs = dell(x)
    if len(last_8(divs)) > 0:
        print(x, min(last_8(divs)))
        cnt += 1
    if cnt == 5:
        break