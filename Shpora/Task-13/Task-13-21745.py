from ipaddress import *

ip1 = ip_address('95.24.2.9')
ip2 = ip_address('95.24.3.10')
ans = []
for m in range(17, 30):
    net1 = ip_network(f'{ip1}/{m}', False)
    net2 = ip_network(f'{ip2}/{m}', False)
    if net1 != net2:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                cnt_1,cnt_2 = 0, 0
                for i in list(net1)[1:-1]:
                    ip = f'{i:b}'
                    if ip[-1] == '0':
                        cnt_1 += 1
                for i in list(net2)[1:-1]:
                    ip = f'{i:b}'
                    if ip[-1] == '0':
                        cnt_2 += 1
                ans.append(cnt_1)
                ans.append(cnt_2)

print(max(ans))