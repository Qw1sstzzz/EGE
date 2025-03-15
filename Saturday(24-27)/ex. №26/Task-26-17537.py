with open('Task-26-17537-file.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (x[1], -x[0]))
hall = [M + 1] * (K + 1)
for h, v in places:
    hall[v] == h

print(places[:10])