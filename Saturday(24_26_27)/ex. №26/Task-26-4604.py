with open('Task-26-4604.txt') as file:
    N = int(file.readline().strip())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
res = [data[0]]

for i in range(1, N - 1):
    if res[-1] - 3 >= data[i]:
        res.append(data[i])

print(len(res), min(res))

# 2767 51