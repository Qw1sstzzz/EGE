from itertools import *

alph = sorted('ЦАПЛЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    s = ''.join(val)
    if s.count('А') <= 1 and s.count('Ц') == 2 and s.count('Л') == 0:
        print(pos, s)
        break