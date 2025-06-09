with open('24.txt') as f:
    data  = []
    for i in f:
        data.append(i.strip())

ans = []

for i in range(len(data)):
    count = dict()
    cnt_N = 0
    for c in data[i]:
        if c == 'N':
            cnt_N += 1
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1

    maxi = count.items()
    maxi = sorted(maxi, key=lambda x: (-x[1], -ord(x[0])))
    ans.append([cnt_N, maxi[0], i])

ans = sorted(ans, key=lambda x: (x[0], x[2]))
print(ans[0][1][0])
