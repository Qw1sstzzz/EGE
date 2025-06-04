from ipaddress import *

ip1 = ip_address('143.168.72.213')

net = ip_network(f'{ip1}/255.255.255.240', False)
if ip1 in net.hosts():
    print(max(net.hosts()))
