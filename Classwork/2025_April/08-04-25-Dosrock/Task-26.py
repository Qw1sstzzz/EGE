with open('Task-26-file.txt') as f:
    N = int(f.readline())
    boxes = [int(i) for i in f]

boxes = sorted(boxes, reverse=True)
presents = [boxes[0]]

for i in boxes:
    if presents[-1] - i >= 9:
        presents.append(i)

print(len(presents), presents[-1])