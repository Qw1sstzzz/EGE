from ipaddress import *

ip = ip_address('203.155.64.0')
for mask in range(0, 32):
    net = ip_network(f'203.155.64.98/{mask}', 0)
    if ip in net:
        print(mask)

# 25