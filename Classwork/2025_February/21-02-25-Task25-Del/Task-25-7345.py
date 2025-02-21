from fnmatch import fnmatch

cnt = 0
positions = [61]
for i in range(1, 10_000):
    positions.append(positions[-1] + 60)

for x in range(88006 - 88006 % 4546, 10**10, 4546):
    if fnmatch(str(x), '8*80*06'):
        cnt += 1
    if cnt in positions:
        print(x, x//4546)