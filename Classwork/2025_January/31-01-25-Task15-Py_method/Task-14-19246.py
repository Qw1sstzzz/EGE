from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:25]

for x in alph:
    s1 = int(f'11353{x}12', 25)
    s2 = int(f'135{x}21', 25)
    if (s1 + s2) % 24 == 0:
        print(x, (s1 + s2) // 24)

# 266249847