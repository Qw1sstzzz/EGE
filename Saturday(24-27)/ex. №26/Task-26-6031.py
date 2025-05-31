with open('Task-26-6031-file.txt') as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data)[::-1]
boxes = [data[0]]

for i in range(1, N):
    if boxes[-1] - data[i] >= 6:
        boxes.append(data[i])

print(len(boxes), min(boxes))