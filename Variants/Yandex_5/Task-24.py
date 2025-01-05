with open('Task-24-file.txt') as file:
    data = file.readline().strip()
maxi = 0
for i in range(len(data)):
    r = data[i]
    for j in range(i + 1, len(data) - 1):
        if r.count(data[j]) == 0:
            r += data[j]
        else:
            maxi = max(len(r), maxi)
            break
print(maxi)

# 17