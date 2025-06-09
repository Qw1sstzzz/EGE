def dell(x):
    r = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            r |= {i, x // i}
    return sorted(r)

ans = []
for x in range(120_115, 120_201):
    divs = dell(x)
    ans.append([len(divs), x])

print(max(ans))

