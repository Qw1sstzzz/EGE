from itertools import groupby

with open('Task-26-2717-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)
ans = []
for pos, places in groupby(data, key=lambda x: x[0]):
    places = list(places)
    if len(places) >= 5:
        for i in range(len(places) - 4):
            places_5 = places[i:i+5]
            if places_5[-1][1] - places_5[0][1] <= 12:
                for j in range(4):
                    if places_5[j+1][1] - places_5[j][1] >= 4:
                        continue
                else:
                    ans.append(places_5)

print(min(ans)[-1])

# 1234 38468



