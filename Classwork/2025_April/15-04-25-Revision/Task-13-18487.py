from ipaddress import *

for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    for ip in net:
        ip = f'{ip:b}'
        if not (ip.count('1') > 15):
            break
    else:
        print(A)
        break