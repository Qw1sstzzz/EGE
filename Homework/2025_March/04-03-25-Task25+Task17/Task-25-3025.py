def nechet(num):
    if num % 2 != 0: return True
    return False

def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if nechet(i): r |= {i}
            if nechet(num//i): r |= {num//i}
    return sorted(r)

def D(arr):
    if len(arr) < 6: return 0
    return arr[-6]

cnt = 0
for x in range(200_000_001, 10**10):
    divs = dell(x)
    d = D(divs)
    if d > 0:
        print(x, d)
        cnt += 1
    if cnt == 5:
        break