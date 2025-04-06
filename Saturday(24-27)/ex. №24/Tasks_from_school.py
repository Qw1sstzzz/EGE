with open('Task-24-1-3-Counter.txt') as f:
    data = f.readline().strip()

# 1
'''
cnt = 0
for i in range(len(data)):
    if cnt == 1000:
        print(i)
        break
    if data[i] == ')':
        cnt += 1
# 1998
'''

# 2
'''
cnt = 0
for i in range(len(data)):
    if cnt == 100:
        print(i)
        break
    if data[i] == '(':
        cnt += 1
# 197
'''

# 3
'''
cnt = 0
for i in range(len(data) - 1):
    if cnt == 10000:
        print(i)
        break
    if data[i] + data[i+1] == '()':
        cnt += 1
# 39621
'''

with open('Task-24-4-8-Counter.txt') as file:
    data = file.readlines()

# 4
'''
ans = 0
for i in data:
    i = i.strip()
    if i.count('O') > i.count('C'):
        ans += 1
print(ans)
# 386
'''

# 5
'''
ans = 0
for i in data:
    i = i.strip()
    if i.count('S') == i.count('X'):
        ans += 1
print(ans)
# 36
'''

# 6
'''
ans = 0
for i in data:
    i = i.strip()
    if i.count('AB') > 2:
        ans += 1
print(ans)
# 163
'''

# 7
'''
ans = 0
for i in data:
    i = i.strip()
    cnt = 0
    for j in range(len(i) - 2):
        if i[j] + i[j + 2] == 'AB':
            cnt += 1
    if cnt > 5:
        ans += 1
print(ans)
# 5
'''

# 8
'''
ans = 0
for i in data:
    i = i.strip()
    cnt = 0
    for j in range(len(i) - 3):
        if i[j] + i[j + 3] == 'ER':
            cnt += 1
    if cnt > 3:
        ans += 1
print(ans)
# 49
'''
