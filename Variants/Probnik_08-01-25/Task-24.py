from string import ascii_uppercase

with open('Task-24-11636-file.txt') as file:
    data = file.readline().strip()

A_first = data.find('A')
A_last = data.rfind('A')
data = data[A_first:A_last+1]

for i in ascii_uppercase[1:]:
    data = data.replace(i, 'B')

while 'BB' in data: data = data.replace('BB', 'B') # Оптимизация, еее)

count_A = data.count('A') # Всего A

kolvo_podstrok = sum(range(1, count_A))

'''
'ABA' -----> kol-vo: count(A) - 1 + count(A) - 2 .. = 1 (+ 0) = 1
'ABABA' ---> kol-vo: count(A) - 1 + count(A) - 2 .. = 2 + 1 (+ 0) = 3
'ABABABA' -> kol-vo: count(A) - 1 + count(A) - 2 .. = 3 + 2 + 1 (+ 0) = 6
'''

ban = 0     # Смотрим, чтобы не было слипшихся AA
for i in range(len(data) - 1):
    if data[i]  + data[i+1] == 'AA':
        ban += 1

print(kolvo_podstrok - ban)
