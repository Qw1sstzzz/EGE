def is_prime(num):
    if num < 2: return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i): r.add(i)
            if is_prime(num // i): r.add(num // i)
    return sorted(r)

def S(arr):
    if len(arr) < 1: return 0
    return sum(arr)

cnt = 0
for x in range(32_500_001, 10**10):
    divs = dell(x)
    s = S(divs)
    if s != 0 and s % 145 == 0:
        print(x, s)
        cnt += 1
    if cnt == 7:
        break

