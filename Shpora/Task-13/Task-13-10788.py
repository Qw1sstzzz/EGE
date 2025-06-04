from ipaddress import *

ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')
cnt = 0

for m in range(0, 33):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 == net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                if f'{net1.network_address:b}'.count('1') >= 5:
                    cnt += 1
print(cnt)