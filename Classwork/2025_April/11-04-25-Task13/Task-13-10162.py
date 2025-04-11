from ipaddress import *

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')

for m in range(17, 33):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 == net2:
        print(net1.netmask)