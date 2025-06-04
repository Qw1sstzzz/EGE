from ipaddress import *

ip1 = ip_address('216.54.187.235')
ip2 = ip_address('216.54.174.128')

for m in range(17, 31):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 != net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                print(m)
