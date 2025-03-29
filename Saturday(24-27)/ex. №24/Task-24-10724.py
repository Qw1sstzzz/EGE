from string import digits, ascii_uppercase
with open('Task-24-10724-file.txt') as f:
    data = f.readline().strip()

alph = '0123456789ABCDEF'
for c in '123456789ABCDEF':
    data = data.replace(c, '*')

for i in 'GHIJKLMNOPQRSTUVWXYZ':
    data = data.replace(i, ' ')

data = data.replace(' 0', ' ')
data = data.split()

print(len(max(data, key=len)))