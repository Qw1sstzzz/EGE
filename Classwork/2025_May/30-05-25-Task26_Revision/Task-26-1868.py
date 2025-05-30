with open('Task-26-1868-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for i in range(N - 1):
    s1, s2 = data[i], data[i+1]
    if s1[0] == s2[0]:
        if s2[1] - s1[1] - 1 == 2:
            print(s1[0], s1[1] + 1)
            break