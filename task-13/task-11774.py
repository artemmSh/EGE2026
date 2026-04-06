from ipaddress import *

cnt = 0

net = ip_network('214.96.0.0/255.240.0.0', False)
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('0') % 3 == 0:
        cnt += 1
print(cnt)
