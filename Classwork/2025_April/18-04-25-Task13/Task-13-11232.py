from ipaddress import *

net = ip_network('192.168.31.80/255.255.255.240', False)
m = 0
for ip in net:
    ip = f'{int(ip):032b}'
    m = max(ip.count('1'), m)

print(m)