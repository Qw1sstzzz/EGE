from string import digits, ascii_uppercase
def convert(num, sys):
    r = ''
    alph = digits + ascii_uppercase
    while num:
        r += alph[num % sys]
        num //= sys
    return r[::-1]

for x in range(1, 10_000):
    num = 7**666 + 7**333 + 49**x - 343
    s = convert(num, 7)
    if s.count('6') == 49:
        print(x)
        break