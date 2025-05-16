for x in range(1, 10_000)[::-1]:
    n = 6**900 + 6**10 - x
    cnt_3 = cnt_5 = 0
    while n:
        if n % 6 == 3:
            cnt_3 += 1
        if n % 6 == 5:
            cnt_5 += 1
        n //= 6
    if cnt_3 == cnt_5:
        print(x)
        break