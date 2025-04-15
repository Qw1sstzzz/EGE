from ipaddress import *

for A in range(0, 256)[::-1]:
    net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            break
    else:
        print(A)
        break