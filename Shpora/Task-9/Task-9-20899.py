with open('Task-9-20899-file.txt')as f:
    data = [list(map(int, i.split())) for i in f]

def f1(arr):
    maxi = max(arr)
    if maxi < sum(arr) - maxi:
        return True
    return False

def f2(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(2) == 2:
        return True
    return False

cnt = 0
for val in data:
    if f1(val) and f2(val):
        cnt += 1
print(cnt)