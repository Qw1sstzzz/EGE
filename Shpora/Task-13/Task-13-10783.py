from ipaddress import *

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
ans = []

for m in range(0, 33):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 == net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                ans.append(net1.num_addresses)

print(min(ans))