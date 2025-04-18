from ipaddress import *
ip1 = ip_address('143.131.211.37')
for m in range(33):
    net = ip_network(f'{ip1}/{m}', False)
    if ip1 not in (net.broadcast_address, net.network_address):
        cnt = 0
        for i in net:
            i = f'{int(i):032b}'
            if i.count('1') == 10:
                cnt += 1
            if cnt > 15:
                break
        if cnt == 15:
            print(m)