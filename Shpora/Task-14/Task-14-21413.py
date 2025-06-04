from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:21]:
    n1 = int(f'82934{x}2', 21)
    n2 = int(f'2924{x}{x}7', 21)
    n3 = int(f'67564{x}8', 21)
    if (n1 + n2 + n3) % 20 == 0:
        print(x, (n1 + n2 + n3) // 20)