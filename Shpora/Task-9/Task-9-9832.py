with open('Task-9-9832-file.txt') as f:
    data = [list(map(int, i.split())) for i in f]

def f1(arr):
    cnt = [arr.count(i) for i in arr]
    if cnt.count(1) == 3 and cnt.count(2) == 4:
        return True
    return False

def f2(arr):
    maxi = max(arr)
    if arr.count(maxi) == 1:
        return True
    return False
ans = []
for pos, arrange in enumerate(data, start=1):
    if f1(arrange) and f2(arrange):
        ans.append([pos, sum(arrange)])

print(min(ans))