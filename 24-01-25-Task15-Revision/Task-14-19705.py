def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

res = []
for x in range(1, 2005):
    num = 43**56 + 113**841 - x
    s = convert(num, 4)
    count_ch = (len([i for i in s if int(i) % 2 == 0]) % 2 == 0)
    count_nch = (len([i for i in s if int(i) % 2 != 0]) % 2 == 0)
    count_2 = (s.count('2') <= 712)
    if count_nch and count_ch and count_2:
        res.append(x)
print(max(res))
