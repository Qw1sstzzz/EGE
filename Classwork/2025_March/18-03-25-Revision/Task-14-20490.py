def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

for x in range(1, 2006)[::-1]:
    n = 4**163 * 5 + 12**62 - x
    s = convert(n ,5)
    if s.count('1') < s.count('4'):
        print(x)
        break
