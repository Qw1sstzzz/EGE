from ipaddress import *

ip1 = ip_address('143.172.12.114')
ips = ip_address('143.172.8.0')
for m in range(16, 33):
    net = ip_network(f'{ip1}/{m}', False)
    if ips == net.network_address:
        print(m, net.netmask)
