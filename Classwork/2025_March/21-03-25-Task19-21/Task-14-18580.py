from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:25]:
    s1 = int(f'A4{x}7F2', 25)
    s2 = int(f'N{x}G5{x}H', 25)
    s3 = int(f'74{x}M26', 25)
    if (s1 + s2 + s3) % 24 == 0:
        print(x, (s1 + s2 + s3) // 24)