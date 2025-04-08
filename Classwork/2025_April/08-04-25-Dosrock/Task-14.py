from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:21]:
    s1 = int(f'82934{x}2', 21)
    s2 = int(f'2924{x}{x}7', 21)
    s3 = int(f'67564{x}8', 21)
    if (s1 + s2 + s3) % 20 == 0:
        print(x, (s1 + s2 + s3) // 20)