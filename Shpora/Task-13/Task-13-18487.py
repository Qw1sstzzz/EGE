from ipaddress import *

for A in range(0, 256):
    ip1 = ip_address(f'192.214.{A}.184')
    net = ip_network(f'{ip1}/255.255.255.224', False)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip.count('1') <= 15:
            break
    else:
        print(A)