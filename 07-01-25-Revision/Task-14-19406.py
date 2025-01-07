from collections import Counter
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def most_common(st):
    lt = sorted(Counter(st).most_common())
    temp = []
    for i in lt:
        v1 = i[1]
        temp.append(v1)
    if temp.count(max(temp)) == 1:
        return (Counter(st).most_common(1))[0][0]
    else:
        rs = []
        for i in range(len(lt)):
            v1, v2 = lt[i][0],lt[i][1]
            rs.append([v2, v1])
        t = []
        for i in rs:
            if i[0] in rs[0]:
                t.append(int(i[1]))
        return max(t)

for x in alph[1:35]:
    s1 = int(f'6{x}QR{x}', 35)
    s2 = int(f'{x}59SH', 35)
    s3 = int(f'PH{x}69YW', 35)
    res = s1 + s2 + s3
    res_copy = str(res)
    mostly = int(most_common(res_copy))
    if res % (mostly ** 2) == 0:
        print(x, res // (mostly ** 2))