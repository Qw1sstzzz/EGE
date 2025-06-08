alph = '01234567'

for y in alph[1:]:
    for x in alph:
        n1 = int(f'{y}04{x}5', 11)
        n2 = int(f'253{x}{y}', 8)
        if (n1 + n2) % 117 == 0:
            print((n1 + n2) // 117)