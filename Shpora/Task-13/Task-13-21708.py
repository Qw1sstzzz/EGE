from ipaddress import *

net = ip_network('11.92.135.56/255.224.0.0', False)
ip1 = ip_address('11.92.135.56')
if ip1 not in (net.network_address, net.broadcast_address):
    for ip in list(net)[::-1]:
        print(1195255254)
        break