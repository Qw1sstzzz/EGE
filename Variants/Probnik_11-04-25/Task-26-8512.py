with open('Task-26-8512-file.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (x[0], x[1]))
approved = [0] * K
