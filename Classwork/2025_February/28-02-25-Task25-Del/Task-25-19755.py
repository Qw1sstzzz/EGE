def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dell(num):
    r = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            r |= {i, num // i}
    return sorted(r)

def M(arr):
    ans = []
    if len(arr) < 1:
        return 0
    else:
        for j in arr:
            if is_prime(j):
                ans.append(j)
        return ans[0] + ans[-1]

cnt = 0
for x in range(1_200_001, 10**10):
    divs = dell(x)
    m = M(divs)
    if m > 2_000 and m % 10 == 8:
        print(x, m)
        cnt += 1
    if cnt == 5:
        break