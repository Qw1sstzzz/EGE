from ipaddress import *

ip1 = ip_address('111.81.192.0')

for m in range(17, 33):
    net = ip_network(f'111.81.208.27/{m}', 0)
    if net.network_address == ip1:
        print(m, net.netmask)