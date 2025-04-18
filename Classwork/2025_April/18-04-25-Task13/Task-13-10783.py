from ipaddress import *

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
ans = []
for m in range(32, 17, -1):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 == net2:
        ans.append(net1.num_addresses)

print(min(ans))