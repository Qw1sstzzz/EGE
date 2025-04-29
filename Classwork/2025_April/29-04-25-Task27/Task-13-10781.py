from ipaddress import *
ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for m in range(17, 30)[::-1]:
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 == net2:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.num_addresses)