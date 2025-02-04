from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

for p in range(2, 37):
    s1 = alph.index('B')*p + alph.index('O')
    s2 = alph.index('O')*p + alph.index('M')
    s3 = alph.index('B')*p**2 + alph.index('L')*p + 4
    s4 = alph.index('C')*p**2 + alph.index('N')*p + alph.index('G')
    if (s1 + s2 + s3) == s4:
        print(p)