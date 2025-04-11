from ipaddress import *

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

for m in range(25, 33)[::-1]:
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1.network_address == net2.network_address:
        print(net1.num_addresses)
        break