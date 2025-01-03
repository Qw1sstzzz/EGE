from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for A in range(1, 10000000):
    for x in alph[:15]:
        M = int(f'432{x}3', 15)
        N = int(f'86{x}86', 15)
        if (M + A) % N == 0:
            print(A)
            break
print('')
print('212298')