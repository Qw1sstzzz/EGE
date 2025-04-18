from ipaddress import *

for A in range(256):
    net = ip_network(f'217.109.{A}.94/255.255.254.0', False)
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('0') > ip[16:].count('0'):
            break
    else:
        print(A)