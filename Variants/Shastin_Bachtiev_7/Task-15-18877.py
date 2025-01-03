def f(x, y, A):
    return (not ((x < 7) or (y >= (5*x + A - 60)) or (x >= 36) or (y < 225)))

for A in range(0, 150)[::-1]:
    if all(f(x, y, A) == 0 for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
print('')
print('110')

