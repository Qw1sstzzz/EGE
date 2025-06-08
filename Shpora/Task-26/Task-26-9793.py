with open('Task-26-9793-file.txt') as f:
    N = int(f.readline())
    details = []
    for pos, i in enumerate(f, start=1):
        sh, ok = map(int, i.split())
        details.append([sh, 'sh', pos])
        details.append([ok, 'ok', pos])

details = sorted(details)
lenta = [0]*N
last = 0

for time, tip, num in details:
    if num not in lenta:
        if tip == 'sh':
            vacant = lenta.index(0)
            lenta[vacant] = num
            last = num
        else:
            vacant = N - lenta[::-1].index(0) - 1
            lenta[vacant] = num
            last = num

print(last, lenta.index(last))