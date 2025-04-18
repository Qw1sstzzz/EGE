from ipaddress import *

ip1 = ip_address('123.20.103.136')
ip2 = ip_address('123.20.103.151')

for m in range(16, 33):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if ip1 != net1.broadcast_address and ip2 != net2.broadcast_address:
        if net1 != net2:
            print(m, net1.netmask)