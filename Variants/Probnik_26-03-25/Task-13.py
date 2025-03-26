from ipaddress import *
ip = ip_address('192.168.24.64')
for m in range(33):
    net = ip_network(f'192.168.24.112/{m}', 0)
    if ip in net:
        mask = f'{net.netmask:b}'
        print(m, mask[16:].count('1'))

# 9 ?