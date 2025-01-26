from itertools import *

alph = sorted('ПРИВЫЧКА')
temp = []
for pos, i in enumerate(product(alph, repeat=5), start = 1):
    i = ''.join(i)
    if pos % 5 == 0:
        continue
    temp.append(i)

for l in range(len(temp)):
    # Так как начинается с 0, то +1 (Первый в списке = позиция 0)
    if len(temp[l]) == len(set(temp[l])):
        if temp[l].count('И') + temp[l].count('Ы') + temp[l].count('А') == 0:
            print(l + 1, temp[l])
            break

# 4754 ВКПЧР