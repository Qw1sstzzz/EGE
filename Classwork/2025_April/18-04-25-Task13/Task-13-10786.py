from ipaddress import *

ip1 = ip_address('151.172.115.121')
ip2 = ip_address('151.172.115.156')

for m in range(17, 33):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 != net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                print(m)