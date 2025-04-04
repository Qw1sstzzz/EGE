def convert(num):
    r = ''
    while num:
        r += str(num % 3)
        num //= 3
    return r[::-1]

for x in range(1, 2031)[::-1]:
    n = 3**100 - x
    s = convert(n)
    if s.count('0') == 1:
        print(x)
        break