from ipaddress import *

for m in range(16, 33):
    net = ip_network(f'99.8.254.232/{m}', False)
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('1') > ip[16:].count('1'):
            break
    else:
        print(m)
print('1'*21 + '0'*11)
print(int('11111000', 2))