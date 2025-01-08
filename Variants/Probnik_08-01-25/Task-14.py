from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:26]:
    s1 = int(f'27{x}98876', 26)
    s2 = int(f'26{x}51', 26)
    s3 = int(f'15{x}47', 26)
    s4 = int(f'62{x}5', 26)
    if (s1 + s2 + s3 + s4) % 25 == 0:
        print(x, (s1 + s2 + s3 + s4) // 25)