from ipaddress import *

for m in range(17, 31):
    ip1 = ip_address(f'127.63.67.1')
    net = ip_network(f'{ip1}/{m}', False)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            break
    else:
        print(m, net.netmask)