for x in range(1, 2031):
    n = 6**260 + 6**160 + 6**60 - x
    cnt0 = 0
    while n:
        if n % 6 == 0:
            cnt0 += 1
        n //= 6
    if cnt0 == 202:
        print(x)
        break