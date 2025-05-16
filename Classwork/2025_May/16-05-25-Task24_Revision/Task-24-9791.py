from string import ascii_uppercase

with open('Task-24-9791-file.txt') as f:
    data = f.readline()

for c in ascii_uppercase[6:]:
    data = data.replace(c, ' ')

data = data.split()

ans = 0
for i in data:
    s = i.lstrip('0')
    if int(s, 16) % 20 == 0:
        ans = max(ans, len(s))
    else:
        for st in range(len(s)):
            for end in range(st + 1, len(s) + 1):
                ps = s[st:end]
                if int(ps, 16) % 20 == 0:
                    ans = max(ans, len(ps))

print(ans)