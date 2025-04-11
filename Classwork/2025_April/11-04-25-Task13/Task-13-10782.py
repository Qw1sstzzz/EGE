from ipaddress import *

ip1 = ip_address('118.187.59.255')
ip2 = ip_address('118.187.65.115')

for m in range(17, 33)[::-1]:
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 != net2:
        if ip1 != net1.network_address and ip1 != net1.broadcast_address:
            if ip2 != net2.network_address and ip2 != net2.broadcast_address:
                print(m)
                break
