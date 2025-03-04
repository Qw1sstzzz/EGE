def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num // i}
    return sorted(r)

def mult(arr):
    c = 1
    for i in arr:
        c *= i
    return c

cnt = 0
for x in range(800_001, 10**20):
    divs = dell(x)
    summ = sum(divs)
    multiply = mult(divs)
    if (summ % 2 != 0) and (multiply % 2 != 0):
       if len(divs) >  10:
           print(x, len(divs))
           cnt += 1
    if cnt  == 6:
        break