from ipaddress import *

ip1 = ip_address('127.63.67.1')

for m in range(16, 33):
    net = ip_network(f'{ip1}/{m}', 0)
    for ip in net:
        if not (f'{ip:b}'[:16].count('1') >= \
                f'{ip:b}'[16:].count('1')):
            break
    else:
        print(m)
        break

print(int('11110000', 2))