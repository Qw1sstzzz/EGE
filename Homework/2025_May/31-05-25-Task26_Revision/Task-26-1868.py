with open('Task-26-1868-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for i in range(N - 1):
    seat1, seat2 = data[i], data[i+1]
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] - 1 == 2:
            print(seat2[0], seat1[1] + 1)
            break