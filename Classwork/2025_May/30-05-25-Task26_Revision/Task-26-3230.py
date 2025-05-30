with open('Task-26-3230-file.txt') as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (-x[0], x[1]))

for i in range(len(data) - 1):
    tree1, tree2 = data[i], data[i+1]
    if tree1[0] == tree2[0]:
        if tree2[1] - tree1[1] == 11:
            print(tree2[0], tree1[1] + 1)
            break

