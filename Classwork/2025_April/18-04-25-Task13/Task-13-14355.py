from ipaddress import *

for m in range(17, 33):
    net = ip_network(f'127.63.67.1/{m}', False)
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            break
    else:
        print(m, net.netmask)