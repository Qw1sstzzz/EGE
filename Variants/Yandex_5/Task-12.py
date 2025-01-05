def even(num):
    r = 1
    for i in num:
        if int(i) % 2 != 0:
            r *= int(i)
    return r

for n in range(4, 10_000):
    s = '0' + n * '5'
    while '55' in s or '150' in s or '555' in s:
        s = s.replace('55', '615', 1)
        s = s.replace('150', '5950', 1)
        s = s.replace('555', '50', 1)
    if even(s) > 100_000:
        print(n)
        break

# 9