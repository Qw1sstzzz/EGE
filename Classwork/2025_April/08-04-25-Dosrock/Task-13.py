from ipaddress import *

net = ip_network('143.168.72.213/255.255.255.240', 0)
for ip in net:
    print(ip)
print(14316872222)