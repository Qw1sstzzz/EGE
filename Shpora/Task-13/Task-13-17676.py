from ipaddress import *

net = ip_network('115.192.0.0/255.192.0.0', False)
cnt = 0

for i in net:
    ip = f'{int(i):032b}'
    if ip.count('1') % 3 != 0:
        cnt += 1

print(cnt)