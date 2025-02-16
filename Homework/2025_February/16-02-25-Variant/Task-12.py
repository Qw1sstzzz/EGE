for n in range(4, 10_000):
    s = '5' + n*'2'
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    summi = sum(map(int, s))
    if summi % 10 == 7:
        print(n, s, summi)
        break

# 5