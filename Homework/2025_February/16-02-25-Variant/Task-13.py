from ipaddress import *

net = ip_network('101.157.240.0/255.255.252.0')
cnt = 0

for i in net:
    ip = f'{i:b}'
    n1 = ip[:16].count('1')
    n2 = ip[16:].count('1')
    if n1 > n2:
        cnt += 1
print(cnt)