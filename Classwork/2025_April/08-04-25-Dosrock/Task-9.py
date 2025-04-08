with open('Task-9-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def checkA(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(3) == 6 and cnt.count(1) == 1:
        return True
    return False

def checkB(arr):
    m = 0
    nepov = 0
    for i in arr:
        if arr.count(i) > 1:
            m = max(m, i)
        if arr.count(i) == 1:
            nepov = i
    if m > nepov:
        return True
    return False

cnt = 0
for i in data:
    if checkA(i) and checkB(i):
        cnt += 1
print(cnt)