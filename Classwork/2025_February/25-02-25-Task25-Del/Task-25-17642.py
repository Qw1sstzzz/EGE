def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num // i}
    return sorted(r)

def last_9(arr):
    r = []
    for i in arr:
        if i != 9 and i % 10 == 9:
            r.append(i)
    return r

cnt = 0
for x in range(800_001, 10**10):
    divs = dell(x)
    if len(last_9(divs)):
        print(x, min(last_9(divs)))
        cnt += 1
    if cnt == 5:
        break
