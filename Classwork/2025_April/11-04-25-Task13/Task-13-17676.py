from ipaddress import *
from ipaddress import ip_address

net = ip_network('115.192.0.0/255.192.0.0', 0)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 3 != 0:
        cnt += 1
print(cnt)