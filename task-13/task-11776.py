from ipaddress import *

cnt = 0

net = ip_network('235.86.56.0/255.255.248.0', False)
for ip in net:
    ip = f'{int(ip):032b}'
    if ip[-2:] == '11':
        cnt += 1
print(cnt)
