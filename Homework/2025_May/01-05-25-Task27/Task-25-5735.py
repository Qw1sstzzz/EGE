def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num//i}
    return sorted(r)

def f(arr):
    r = [j for j in arr if j in [2**k for k in range(1, 50)]]
    if len(r) >= 20:
        return r
    return []

cnt = 0
for n in range(10**6+1, 10**10):
    divs = dell(n)

    if len(f(divs)) > 0:
        arr = []
        for i in divs:
            if i not in f(divs):
                arr.append(i)
        if len(arr) < 1:
            print(n, 0)
            cnt += 1
        else:
            print(n, sum(arr))
            cnt += 1
    if cnt == 5:
        break