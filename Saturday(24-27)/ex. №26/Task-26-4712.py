with open('Task-26-4712-file.txt') as f:
    N = int(f.readline())
    data = [int(i) for i in f]

# N = 5
# data = [43, 40, 32, 40, 30]

data = sorted(data, reverse=True)

boxes = [data[0]]

for i in range(1, N):
    if boxes[-1] - data[i] >= 3:
        boxes.append(data[i])

print(len(boxes), min(boxes))