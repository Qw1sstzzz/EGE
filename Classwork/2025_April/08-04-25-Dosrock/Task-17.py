with open('Task-17-file.txt') as file:
    data = [int(i) for i in file]

summi_otr = sum([i for i in data if i < 0])
ans = []

for i in range(len(data) - 2):
    t = [data[i], data[i+1], data[i+2]]
    maxi = max(t)
    mini = min(t)
    if maxi*mini > summi_otr:
        ans.append(data[i] + data[i+1] + data[i+2])
print(len(ans), abs(max(ans)))

# 10007 7953