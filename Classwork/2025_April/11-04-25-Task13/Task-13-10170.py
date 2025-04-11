from ipaddress import *

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for m in range(17, 33):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1.network_address != net2.network_address:
        print(m)
        break
print('Количество единиц в третьем байте =', 20 - 2*8)
print(int('1'*4 + '0'*4, 2))

