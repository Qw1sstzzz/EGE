def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            r |= {i, num // i}
    return sorted(r)

def M(arr):
    if len(arr) < 2:
        return 0
    return arr[-2] + arr[-1]

for N in range(112_500_000, 112_550_000):
    divs = dell(N)
    m = M(divs)
    if str(m)[-4:] == '1214':
        print(N)
