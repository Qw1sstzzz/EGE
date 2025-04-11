from ipaddress import *

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for m in range(17, 33):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 != net2:
        print(m)
        break
