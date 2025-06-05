with open('Task-17-21416-file.txt') as f:
    data = [int(i) for i in f]

summ_otr = sum([i for i in data if i < 0])
ans = []

for i in range(len(data) - 2):
    p1, p2, p3 = data[i:i+3]
    maxi = max(p1, p2, p3)
    mini = min(p1, p2, p3)
    if maxi * mini > summ_otr:
        ans.append(p1 + p2 + p3)

print(len(ans), abs(max(ans)))