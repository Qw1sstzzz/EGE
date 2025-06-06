with open('test.txt') as f:
    N = int(f.readline())
    data = dict()
    Avg_price = sum([int(i.split()[1]) for i in f]) / N
    for i in f:
        line = i.split()
        print(line)
        ID = int(line[0])
        price = int(line[1])
        state = int(line[2])


print(data)


