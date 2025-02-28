def N(k):
    return 750_000 + k

def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i % 2 == 0: r.add(i)
            if num//i % 2 == 0: r.add(num//i)
    return sorted(r)

cnt = 0
for k in range(1, 10**10):
    n = N(k)
    divs = dell(n)
    if len(divs) % 2 != 0:
        print(k, len(divs))
        cnt += 1
    if cnt == 5:
        break