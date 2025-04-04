def convert(num):
    r = ''
    while num:
        r += str(num % 7)
        num //= 7
    return r[::-1]

for x in range(1, 10_000):
    n = 7**666 + 7**333 + 49**x - 343
    s = convert(n)
    if s.count('6') == 49:
        print(x)
        break