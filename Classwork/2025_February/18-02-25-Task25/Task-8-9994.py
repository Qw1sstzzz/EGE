from itertools import product

alph = sorted('ШКОЛА')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    s = ''.join(val)
    if s == 'ШАЛАШ':
        print(pos, s)
        break