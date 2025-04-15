from ipaddress import *

ip1 = ip_address('218.48.192.0')
cnt = 0
for m in range(17, 33):
    net = ip_network(f'218.48.192.56/{m}', 0)
    if ip1 == net.network_address:
        if net.num_addresses >= 500:
            cnt += 1
print(cnt)

