from ipaddress import *

for m in range(17, 30)[::-1]:
    net = ip_network(f'238.51.1.202/{m}', False)
    if ip_address('238.51.1.202') not in (net.network_address, net.broadcast_address):
        for ip in net:
            s = f'{ip:b}'
            if s[:16].count('1') < s[16:].count('1'):
                break
        else:
            print(net.netmask)