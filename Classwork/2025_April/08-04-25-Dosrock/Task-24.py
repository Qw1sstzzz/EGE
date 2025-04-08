from string import digits, ascii_uppercase

with open('Task-24-file.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase
for c in alph[12:]:
    data = data.replace(c, ' ')

ans = [[0, '1']]
while ' 0' in data:
    data = data.replace(' 0', ' ')
data = data.split()

for i in data:
    if len(i) > max(ans)[0]:
        while len(i) > 2 and int(i, 12) % 2 != 0:
            i = i[:-1]
            if int(i, 12) % 2 == 0:
                ans.append([len(i), i])
                break
            else:
                continue
print(max(ans)[0])


