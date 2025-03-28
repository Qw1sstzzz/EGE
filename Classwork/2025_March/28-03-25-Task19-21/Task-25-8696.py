def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def M(arr):
    if len(arr) == 0: return 0
    return sum(arr)
cnt = 0

for x in range(1_273_548, 10**10):
    divs = dell(x)
    m = M(divs)
    n = m % 100_000
    if m != 0 and is_prime(n):
        print(x, m)
        cnt += 1
    if cnt == 5:
        break