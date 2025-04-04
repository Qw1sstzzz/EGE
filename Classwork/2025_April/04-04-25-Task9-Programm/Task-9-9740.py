from operator import truediv

with open('Task-9-9740-file.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(3) == 3 and cnt.count(1) == 4:
        return True
    return False

def f2(arr):
    avg = sum(arr) / len(arr)
    cnt = [[arr.count(i), i] for i in arr]
    maxi = max(cnt)[1]
    if avg <= maxi:
        return True
    return False

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)

