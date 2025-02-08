with open('Task-26-16390-file.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)

ans = []
mass = 0
for i in data:
    if mass + i <= S:
        ans.append(i)
        mass += i
ans_A = len(ans)

ans_B = 0
for j in data[::-1]:
    if sum(data[0:ans_A-1]) + j <= S:
        ans_B = max(ans_B, j)
print(ans_A, ans_B)

# 2216 56