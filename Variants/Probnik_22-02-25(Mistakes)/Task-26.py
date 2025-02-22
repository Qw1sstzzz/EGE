with open('Task-26-1-file.txt') as file:
    N, S = [int(i) for i in file.readline().split()]
    data = []
    for j in file:
        j = j.split()
        ID = int(j[0])
        ex1 = int(j[1])
        ex2 = int(j[2])
        ex3 = int(j[3])
        sobes = int(j[4])
        balli = ex1 + ex2 + ex3
        data.append([ID, balli, sobes])

data = sorted(data, key=lambda x: (-x[1], -x[2], x[0]))
