from ipaddress import *

ip1 = ip_address('211.115.61.154')
ip2 = ip_address('211.115.59.137')

for m in range(17, 33)[::-1]:
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 == net2:
        print(net1.netmask)
        break