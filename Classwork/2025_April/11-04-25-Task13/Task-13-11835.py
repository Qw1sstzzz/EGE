from ipaddress import *
cnt = 0
for A in range(256):
    net = ip_network(f'207.0.{A}.167/255.255.255.192', 0)
    for ip in net:
        ip = f'{ip:b}'
        if ip[:16].count('0') <= ip[16:].count('0'):
            break
    else:
        cnt += 1
print(cnt)