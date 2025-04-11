from ipaddress import *

print('Уже использовано 16 единичек')

for m in range(17, 33):
    net = ip_network(f'152.65.245.132/{m}', 0)
    for ip in net:
        i = f'{int(ip):032b}'
        if i[:16].count('0') < i[16:].count('0'):
            break
    else:
        print(m)
        break
print(22 - 16)
print(int('11111100',2))