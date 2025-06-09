with open('26.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
ans = []
for i in range(N - 1):
    m1, m2 = data[i], data[i+1]
    if m1[0] == m2[0]:
        if m2[1] - m1[1] - 1 == 1:
            ans.append(m1[0])

res = dict()
for i in ans:
   if i not in res.keys():
       res[i] = 1
   else:
       res[i] += 1

res = res.items()
res = sorted(res, key=lambda x: (-x[1], x[0]))
print(res[0])