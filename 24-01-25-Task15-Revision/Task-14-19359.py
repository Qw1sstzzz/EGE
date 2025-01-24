from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:22]:
    s1 = int(f'A23{x}AC0', 22)
    s2 = int(f'GB{x}21670', 22)
    if (s1 + s2) % 21 == 0:
        print(x, (s1 + s2) // 22)