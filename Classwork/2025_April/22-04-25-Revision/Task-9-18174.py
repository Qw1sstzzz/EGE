with open('Task-9-18174-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def check1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 2 and cnt.count(1) == 4:
        return True
    return False

def check2(arr):
    otr = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    summ_otr = 0
    for i in otr:  summ_otr += abs(i)
    if summ_otr > sum(pos):
        return True
    return False

res = 0
for i in data:
    if check1(i) and check2(i):
        res += 1
print(res)