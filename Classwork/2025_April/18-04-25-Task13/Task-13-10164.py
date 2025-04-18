from ipaddress import *

net = ip_network('156.132.15.138/255.255.252.0', False)

for pos, ip in enumerate(net, start=0):
    if ip == ip_address('156.132.15.138'):
        print(pos)
        break
