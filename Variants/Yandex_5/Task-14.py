from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
res = []
for x in range(0, 190):
    for y in range(0, 190):
        s1 = alph.index('N')*190**2 + x*190 + alph.index('W')
        s2 = alph.index('Y')*190**3 + y*190**2 + alph.index('A')*190 + alph.index('R')
        if (s1 + s2) % 189 == 0:
            res.append([x*y, (s1 + s2)//189])
print(max(res))