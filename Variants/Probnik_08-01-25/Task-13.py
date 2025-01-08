from ipaddress import *

net = ip_network('101.157.240.0/255.255.252.0', 0)
cnt = 0
for ip in net:
    ip = f'{ip:b}'
    ip1 = ip[:16]
    ip2 = ip[16:]
    if ip1.count('1') > ip2.count('1'):
        cnt += 1
print(cnt)