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
            if is_prime(i): r.add(i)
            if is_prime(num // i): r.add(num // i)
    return sorted(r)

def F(arr):
    if len(arr) < 1:
        return 0
    return sum(arr) // len(arr)

cnt = 0
for x in range(650001, 10**100):
    divs = dell(x)
    f = F(divs)
    if f % 37 == 23:
        print(x, f)
        cnt += 1
    if cnt == 4:
        break