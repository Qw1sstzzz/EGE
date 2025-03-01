def is_prime(num):
    if num < 2:
        return False
    for k in range(2, int(num**0.5) + 1):
        if num % k == 0:
            return False
    return True

def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def M(arr):
    if len(arr) < 1: return 0
    else: return sum(arr)

cnt = 0
for x in range(1_273_548, 10**10):
    divs = dell(x)
    m = M(divs)
    if is_prime(m % 100_000):
        print(x, m)
        cnt += 1
    if cnt == 5:
        break