def is_prime(num):
    if num < 2: return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dell(num):
    r = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): r.add(i)
            if is_prime(num // i): r.add(num // i)

    return sorted(r)

def M(arr):
    if len(arr) < 2:
        return 0
    return max(arr) + min(arr)

cnt = 0
for x in range(1_200_001, 10**10):
    divs = dell(x)
    m = M(divs)
    if m > 2000 and m % 10 == 8:
        print(x, m)
        cnt += 1
    if cnt == 5:
        break