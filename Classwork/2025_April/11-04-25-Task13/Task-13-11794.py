from ipaddress import *

for A in range(256)[::-1]:
    ip1 = ip_address(f'223.167.{A}.167')
    net = ip_network(f'{ip1}/255.255.255.192', 0)
    for ip in net:
        i = f'{ip:b}'
        if i[:16].count('0') > i[16:].count('0'):
            break
    else:
        print(A)
        break