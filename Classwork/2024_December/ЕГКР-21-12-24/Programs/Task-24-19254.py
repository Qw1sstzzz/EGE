with open('Task-24-19254-file.txt') as f:
    data = f.readline() + 'FSRQ'.strip()
# Допишем в конец строки FSRQ, чтобы комманда работала и захватывала последнюю возможную подстроку
'''
maxi = 0    # Макс. длина подстроки
data = data.split('FSRQ')       # Разобьём строки по FSQR -> получится список, с которым будем работать
for i in range(len(data) - 81):
    ps = 'FSRQ'.join(data[i:i+81])      # Создаём строку, включая в неё ровно 80 FSRQRQ
    maxi = max(len(ps), maxi)           # Находим длину подстроки
print(maxi+6)
# Прибавляем 6, т.к. "FSRQ**FSRQ***FSRQ" будет возвращать подстроку "**FSRQ***" (а макс: "SRQ**FSRQ***FSR")
'''
# 2
maxi = 0
for i in range(len(data)-4):
    cnt = data[i:i + 4]
    ban = 0
    ps = data[i:i + 4]
    if ps == 'FSRQ':
        pass
    for j in range(i+4, len(data)):
        cnt += data[j]
        if cnt.count('FSRQ') == 81:
            maxi = max(len(cnt)-1, maxi)
            break
print(maxi)
