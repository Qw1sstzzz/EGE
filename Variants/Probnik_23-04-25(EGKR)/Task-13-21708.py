from ipaddress import *

ip1 = ip_address('11.92.135.56')

net = ip_network(f'{ip1}/255.224.0.0', False)
ans = []

if ip1 not in (net.broadcast_address, net.network_address):
    for ip in net:
        if ip not in (net.broadcast_address, net.network_address):
            ans.append(ip)
print(ans[-1])