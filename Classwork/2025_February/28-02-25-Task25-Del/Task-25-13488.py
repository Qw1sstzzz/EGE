def dell(num):
    r = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if i % 2 != 0: r |= {i}
            if (num // i) % 2 != 0: r |= {num // i}
    return sorted(r)

for x in range(18782, 18823):
    divs = dell(x)
    if len(divs) == 3:
        print(*divs)