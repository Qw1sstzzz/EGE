from fnmatch import fnmatch
def divs(num):
    cnt = 0
    arr = []
    for x in range(2, round(num**0.5) + 1, 2):
        if num % x == 0:
            cnt += 1
            arr.append(x)
    if cnt >= 4:
        return [1, arr]
    else:
        return [0, arr]

for x in range(65001, 100**100):
    if fnmatch(str(x), '6*97*5?'):
        if divs(x)[0] == 1:
            summi = divs(x)[1]
            summi = sum(summi)
            print(x, summi)
