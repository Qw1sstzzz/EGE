from collections import Counter

with open('Task-17-5758-file.txt') as file:
    data = [int(i) for i in file]

moda = Counter(data).most_common(1)[0][0] # 344
res = []

for i in range(len(data)):
    for j in range(i+1, len(data)):
        ch1, ch2 = data[i], data[j]
        pair = sorted((ch1, ch2))

        if (j - i) % 2 == 0:
            if pair[0] < moda < pair[1]:
                res.append(max(abs(moda - pair[0]), abs(moda - pair[1])))

print(len(res), max(res))