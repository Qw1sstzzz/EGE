with open('Task-9-5489-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def f1(arr):
    if len(set(arr)) == len(arr):
        return True
    return False

def f2(arr):
    ch = [i for i in arr if int(i) % 2 == 0]
    nech = [i for i in arr if int(i) % 2 != 0]
    if len(ch) > len(nech):
        return True
    return False

def f3(arr):
    ch = sum([int(i) for i in arr if int(i) % 2 == 0])
    nech = sum([int(i) for i in arr if int(i) % 2 != 0])
    if nech > ch:
        return True
    return False

cnt = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        cnt += 1
print(cnt)