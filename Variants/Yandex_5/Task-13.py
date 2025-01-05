from ipaddress import *

ip = ip_address('137.219.220.63')

for m in range(33)[::-1]:
    net = ip_network(f'137.219.220.63/{m}', 0)
    if ip != net[-1]:
        print(m)
        break

# 25