with open('Task-9-6262-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def check1(arr):
    count = [arr.count(i) for i in arr]
    if sum(count) > 6:
        return True
    return False

def check2(arr):
    nech = [i for i in arr if i % 2 != 0]
    if len(nech) == 3:
        return True
    return False

cnt = 0
for i in data:
    if check1(i) and check2(i):
        cnt += 1
print(cnt)