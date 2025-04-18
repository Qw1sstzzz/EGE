from ipaddress import *

cnt = 0
for A in range(0, 256):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'246.81.65.{A}/255.255.255.224', 0)
    if ip != net.network_address and ip != net.broadcast_address:
        for i in list(net)[1:-1]:
            i = f'{int(i):032b}'
            if not (i[16:24].count('0') > i[24:].count('0')):
                break
        else:
            cnt += 1
print(cnt)