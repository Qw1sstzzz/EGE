with open('Task-24-19970-file.txt') as file:
    data = file.readline().strip()

def f(s):
    s = s.replace('*', ' ').replace('+', ' ')
    for i in s.split():
        if int(i) % 5 != 0:
            return False
    return True


while '**' in data: data = data.replace('**', '* *')
while '*+' in data: data = data.replace('*+', '* +')
while '+*' in data: data = data.replace('+*', '+ *')
while '++' in data: data = data.replace('++', '+ +')

data = data.replace(' +', ' ').replace('+ ', ' ')
data = data.replace(' *', ' ').replace('* ', ' ')
m = 0

data =  data.split()

for i in data:
    if (len(i) > m) and ((i.count('+') + i.count('*')) >= 1):
        if f(i):
            m = max(m, len(i))
print(m)
