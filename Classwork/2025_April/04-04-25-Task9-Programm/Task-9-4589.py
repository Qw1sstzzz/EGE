with open('Task-9-4589-file.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(arr):
    maxi = max(arr)
    if sum(arr) - maxi > maxi:
        return True
    return False

def f2(arr):
    maxi = max(arr)
    mini = min(arr)
    if (maxi + mini) == (sum(arr) - maxi - mini):
        return True
    return False

cnt = 0
for i in data:
    if f1(i) + f2(i) == 2:
        cnt += 1
print(cnt)
