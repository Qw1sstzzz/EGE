from ipaddress import *

ip = ip_address('153.202.16.37')
ips = ip_address('153.202.16.32')
for m in range(17, 33):
    net = ip_network(f'{ip}/{m}', False)
    if net.network_address == ips:
        print(m, net.netmask)
print(255 + 248)