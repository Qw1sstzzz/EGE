with open('Task-9-9778-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(1) == 4 and cnt.count(2) == 2:
        return True
    return False

def f2(arr):
    cnt = sorted([[arr.count(i), i] for i in arr])
    pov = cnt[-1][1]
    summ = 0
    for i in cnt:
        if i[0] == 1:
            summ += i[1]
    if pov >= (summ / 4):
        return True
    return False

for pos, arrange in enumerate(data, start=1):
    if f1(arrange) and f2(arrange):
        print(pos, arrange)
        break