def convert(num, sys):
    r = ''
    while num:
        r += str(num % sys)
        num //= sys
    return r[::-1]

ans = []
for x in range(1, 2006):
    n = 43 ** 56 + 113**841 - x
    s = convert(n, 4)
    chet = [i for i in s if int(i) in [0, 2]]
    nechet = [i for i in s if int(i) in [1, 3]]
    if len(chet) % 2 == 0 and len(nechet) % 2 == 0:
        if s.count('2') <= 712:
            ans.append(x)

print(max(ans))