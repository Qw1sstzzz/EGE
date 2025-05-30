with open('Task-26-4604-file.txt') as f:
    N = int(f.readline())
    boxes = [int(i) for i in f]

boxes = sorted(boxes, reverse=True)

ans = [boxes[0]]
for i in range(1, N):
    if ans[-1] - boxes[i] >= 3:
        ans.append(boxes[i])

print(len(ans), ans[-1])


