from ipaddress import *

cnt = 0
for A in range(0, 256):
    net = ip_network(f'246.81.65.{A}/255.255.255.224', 0)
    for ip in list(net)[1:-1]:
        ip = f'{int(ip):032b}'
        if not (ip[16:24].count('0') > ip[24:].count('0')):
            break
    else:
        cnt += 1
print(cnt)