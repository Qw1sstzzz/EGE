def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

for N in range(3_000_000, 4_000_000):
    s = convert(N, 3)
    s = s.replace('2', '*').replace('0', '2').replace('*', '0')
    s = s.lstrip()
    R = abs(int(s, 3) - N)
    if R == 1_864_246:
        print(N)
        break