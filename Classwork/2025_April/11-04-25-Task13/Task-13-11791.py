from ipaddress import *

for m in range(17, 33):
    net = ip_network(f'246.51.128.202/{m}', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            break
    else:
        print(m)
        break
print('23 - 16 =', 23 - 16)
print('То есть в третьем байте число, в котором 7 единичек, которые стоят на первых местах')
print(int('1'*7 + '0', 2))