with open('Task-24-1-file.txt') as file:
    data = file.readline().strip()

for c in '23456789':
    data = data.replace(c, '1')

while '**' in data: data = data.replace('**', '* *')
while '*+' in data: data = data.replace('*+', '* +')
while '+*' in data: data = data.replace('+*', '+ *')
while '++' in data: data = data.replace('++', '+ +')
while '+00' in data: data = data.replace('+00', '+0 0')
while '+01' in data: data = data.replace('+01', '+0 1')
while '*00' in data: data = data.replace('*00', '*0 0')
while '*01' in data: data = data.replace('*01', '*0 1')
data = data.split()
m = 0
for i in data:
    if m < len(i):
        i = i.strip('*').strip('+')
        if eval(i) == 0:
            m = max(m, len(i))
print(m)
