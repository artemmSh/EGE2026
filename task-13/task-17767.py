from ipaddress import *

net = ip_network('228.172.236.0/255.255.240.0', False)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 5:
        cnt += 1
print(cnt)
