def dell(num):
    r = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            r.add(i)
            r.add(num//i)
    return sorted(list(r))[:-1]

cnt = 0
for x in range(600_000, 10**8):
    min_div_7 = 0
    divs_x = dell(x)
    for i in divs_x:
        if str(i)[-1] == '7' and i != 7:
            min_div_7 = i
            break
    if min_div_7 != 0:
        print(x, min_div_7)
        cnt += 1
        if cnt == 5:
            break
