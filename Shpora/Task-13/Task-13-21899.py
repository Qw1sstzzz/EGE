from ipaddress import *

net = ip_network('98.81.154.195/255.252.0.0', False)
ip1 = ip_address('98.81.154.195')
if ip1 not in (net.network_address, net.broadcast_address):
    for ip in list(net)[::-1]:
        print(ip)
        input()