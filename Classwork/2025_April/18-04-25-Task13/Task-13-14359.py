from ipaddress import *

ip1 = ip_address('157.127.172.56')
ip2 = ip_address('157.127.191.78')

for m in range(17, 33):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 != net2:
        print(m)